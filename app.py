import os, secrets, hmac, hashlib
from datetime import datetime
from functools import wraps
from flask import Flask, request, redirect, url_for, session, flash, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "")
if not app.config["SECRET_KEY"]:
    raise RuntimeError("Set a strong SECRET_KEY environment variable before starting.")
db_url = os.environ.get("DATABASE_URL", "sqlite:///alhazmi.db")
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)
app.config.update(
    SQLALCHEMY_DATABASE_URI=db_url,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("COOKIE_SECURE", "1") == "1",
    PERMANENT_SESSION_LIFETIME=60 * 60 * 8,
)
db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(180), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(80), default="")
    city = db.Column(db.String(80), default="")
    course = db.Column(db.String(160), default="")
    study_mode = db.Column(db.String(80), default="")
    status = db.Column(db.String(40), default="جديد")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), nullable=False)
    level = db.Column(db.String(80), default="")
    fee = db.Column(db.Integer, default=0)
    duration = db.Column(db.String(80), default="شهر واحد")
    active = db.Column(db.Boolean, default=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(40), default="ريال يمني قديم")
    note = db.Column(db.String(250), default="")
    paid_at = db.Column(db.DateTime, default=datetime.utcnow)
    student = db.relationship("Student", backref="payments")

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    day = db.Column(db.String(60), default="")
    time = db.Column(db.String(80), default="")
    mode = db.Column(db.String(80), default="Zoom")
    notes = db.Column(db.String(250), default="")

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    assessment = db.Column(db.String(160), nullable=False)
    score = db.Column(db.String(40), nullable=False)
    certificate_no = db.Column(db.String(100), default="")
    published = db.Column(db.Boolean, default=False)
    student = db.relationship("Student", backref="results")

def csrf_token():
    if "_csrf" not in session:
        session["_csrf"] = secrets.token_urlsafe(32)
    return session["_csrf"]

@app.context_processor
def inject_globals():
    return {"csrf_token": csrf_token}

@app.before_request
def protect_posts():
    if request.method == "POST":
        supplied = request.form.get("_csrf", "")
        expected = session.get("_csrf", "")
        if not expected or not hmac.compare_digest(supplied, expected):
            abort(400, "طلب غير صالح. حدّث الصفحة وحاول مرة أخرى.")

def admin_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not session.get("admin_id"):
            return redirect(url_for("login", next=request.path))
        return fn(*args, **kwargs)
    return wrapped

@app.route("/")
def home():
    courses = Course.query.filter_by(active=True).order_by(Course.id).all()
    schedules = Schedule.query.order_by(Schedule.id.desc()).limit(8).all()
    return render_template("home.html", courses=courses, schedules=schedules)

@app.route("/register", methods=["POST"])
def register():
    student = Student(
        full_name=request.form.get("full_name", "").strip(),
        phone=request.form.get("phone", "").strip(),
        country=request.form.get("country", "").strip(),
        city=request.form.get("city", "").strip(),
        course=request.form.get("course", "").strip(),
        study_mode=request.form.get("study_mode", "").strip(),
    )
    if not student.full_name or not student.phone:
        flash("يرجى إدخال الاسم ورقم الهاتف.", "error")
        return redirect(url_for("home") + "#register")
    db.session.add(student)
    db.session.commit()
    flash("تم استلام طلب التسجيل. سيتواصل المكتب معك لتأكيد التفاصيل.", "success")
    return redirect(url_for("home") + "#register")

@app.route("/admin/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        admin = Admin.query.filter_by(username=request.form.get("username", "").strip()).first()
        if admin and check_password_hash(admin.password_hash, request.form.get("password", "")):
            session.clear()
            session["admin_id"] = admin.id
            session.permanent = True
            flash("تم تسجيل الدخول.", "success")
            return redirect(url_for("dashboard"))
        flash("اسم المستخدم أو كلمة المرور غير صحيحة.", "error")
    return render_template("login.html")

@app.route("/admin/logout", methods=["POST"])
@admin_required
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/admin")
@admin_required
def dashboard():
    return render_template("dashboard.html",
        students=Student.query.order_by(Student.created_at.desc()).all(),
        courses=Course.query.order_by(Course.id).all(),
        payments=Payment.query.order_by(Payment.paid_at.desc()).limit(12).all(),
        schedules=Schedule.query.order_by(Schedule.id.desc()).all(),
        results=Result.query.order_by(Result.id.desc()).all(),
        student_count=Student.query.count(),
        payment_total=db.session.query(db.func.coalesce(db.func.sum(Payment.amount), 0)).scalar(),
    )

@app.route("/admin/student/add", methods=["POST"])
@admin_required
def add_student():
    s = Student(full_name=request.form.get("full_name","").strip(), phone=request.form.get("phone","").strip(),
                country=request.form.get("country",""), city=request.form.get("city",""),
                course=request.form.get("course",""), study_mode=request.form.get("study_mode",""),
                status=request.form.get("status","جديد"))
    if not s.full_name or not s.phone:
        flash("الاسم ورقم الهاتف مطلوبان.", "error")
    else:
        db.session.add(s); db.session.commit(); flash("تمت إضافة الطالب.", "success")
    return redirect(url_for("dashboard") + "#students")

@app.route("/admin/student/<int:item_id>/status", methods=["POST"])
@admin_required
def student_status(item_id):
    s = Student.query.get_or_404(item_id)
    s.status = request.form.get("status", s.status)
    db.session.commit()
    flash("تم تحديث حالة الطالب.", "success")
    return redirect(url_for("dashboard") + "#students")

@app.route("/admin/student/<int:item_id>/delete", methods=["POST"])
@admin_required
def delete_student(item_id):
    s = Student.query.get_or_404(item_id)
    Payment.query.filter_by(student_id=s.id).delete()
    Result.query.filter_by(student_id=s.id).delete()
    db.session.delete(s); db.session.commit()
    flash("تم حذف سجل الطالب والبيانات المرتبطة به.", "success")
    return redirect(url_for("dashboard") + "#students")

@app.route("/admin/course/add", methods=["POST"])
@admin_required
def add_course():
    c = Course(name=request.form.get("name","").strip(), level=request.form.get("level",""),
               fee=int(request.form.get("fee") or 0), duration=request.form.get("duration","شهر واحد"))
    if c.name:
        db.session.add(c); db.session.commit(); flash("تمت إضافة الدورة.", "success")
    return redirect(url_for("dashboard") + "#courses")

@app.route("/admin/course/<int:item_id>/toggle", methods=["POST"])
@admin_required
def toggle_course(item_id):
    c = Course.query.get_or_404(item_id); c.active = not c.active
    db.session.commit(); return redirect(url_for("dashboard") + "#courses")

@app.route("/admin/payment/add", methods=["POST"])
@admin_required
def add_payment():
    student = Student.query.get_or_404(int(request.form.get("student_id") or 0))
    amount = int(request.form.get("amount") or 0)
    if amount <= 0:
        flash("أدخل مبلغاً صحيحاً.", "error")
    else:
        db.session.add(Payment(student_id=student.id, amount=amount,
                               currency=request.form.get("currency","ريال يمني قديم"),
                               note=request.form.get("note","")))
        db.session.commit(); flash("تم تسجيل الدفعة.", "success")
    return redirect(url_for("dashboard") + "#payments")

@app.route("/admin/schedule/add", methods=["POST"])
@admin_required
def add_schedule():
    title = request.form.get("title","").strip()
    if title:
        db.session.add(Schedule(title=title, day=request.form.get("day",""),
            time=request.form.get("time",""), mode=request.form.get("mode","Zoom"),
            notes=request.form.get("notes","")))
        db.session.commit(); flash("تمت إضافة المحاضرة.", "success")
    return redirect(url_for("dashboard") + "#schedule")

@app.route("/admin/schedule/<int:item_id>/delete", methods=["POST"])
@admin_required
def delete_schedule(item_id):
    db.session.delete(Schedule.query.get_or_404(item_id)); db.session.commit()
    return redirect(url_for("dashboard") + "#schedule")

@app.route("/admin/result/add", methods=["POST"])
@admin_required
def add_result():
    student = Student.query.get_or_404(int(request.form.get("student_id") or 0))
    assessment = request.form.get("assessment","").strip()
    score = request.form.get("score","").strip()
    if assessment and score:
        db.session.add(Result(student_id=student.id, assessment=assessment, score=score,
            certificate_no=request.form.get("certificate_no","").strip(),
            published=bool(request.form.get("published"))))
        db.session.commit(); flash("تم حفظ النتيجة.", "success")
    return redirect(url_for("dashboard") + "#results")

@app.route("/verify")
def verify():
    code = request.args.get("code","").strip()
    result = Result.query.filter_by(certificate_no=code, published=True).first() if code else None
    return render_template("verify.html", result=result, code=code)

@app.errorhandler(400)
def bad_request(error):
    return render_template("error.html", message=str(error.description)), 400

with app.app_context():
    db.create_all()
    # The first admin is created only from deployment environment variables.
    username = os.environ.get("ADMIN_USERNAME")
    password = os.environ.get("ADMIN_PASSWORD")
    if username and password and not Admin.query.filter_by(username=username).first():
        db.session.add(Admin(username=username, password_hash=generate_password_hash(password)))
        db.session.commit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
