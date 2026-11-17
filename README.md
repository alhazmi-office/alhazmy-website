<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مكتب الحزمي لتحضير التوفل والآيلتس | Alhazmi TOEFL & IELTS Preparation Office</title>
    <!-- استيراد خط عربي واحترافي -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <!-- مكتبة الأيقونات FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #0b3c65;
            --secondary-color: #0077b6;
            --accent-color: #90e0ef;
            --bg-color: #f8f9fa;
            --text-color: #333333;
            --white: #ffffff;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Cairo', sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        /* شريط التنقل العلوي */
        header {
            background-color: var(--white);
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .navbar {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 20px;
        }

        .logo-container {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-container h1 {
            font-size: 1.2rem;
            color: var(--primary-color);
            font-weight: 700;
        }

        .logo-container span {
            display: block;
            font-size: 0.8rem;
            color: #666;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 20px;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 600;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--secondary-color);
        }

        .cta-btn {
            background-color: var(--secondary-color);
            color: var(--white);
            padding: 8px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 700;
            transition: background 0.3s;
        }

        .cta-btn:hover {
            background-color: var(--primary-color);
        }

        /* القسم الرئيسي (Hero) */
        .hero {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: var(--white);
            text-align: center;
            padding: 80px 20px;
        }

        .hero h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 30px;
            opacity: 0.9;
        }

        .hero-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
        }

        .btn-light {
            background-color: var(--white);
            color: var(--primary-color);
            padding: 12px 30px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 700;
        }

        /* الأقسام العامة */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 60px 20px;
        }

        .section-title {
            text-align: center;
            margin-bottom: 40px;
            color: var(--primary-color);
            font-size: 2rem;
        }

        /* شبكة المستويات (خارطة الدورات) */
        .levels-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .level-card {
            background: var(--white);
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            padding: 30px;
            border-top: 5px solid var(--secondary-color);
        }

        .level-card h3 {
            color: var(--primary-color);
            margin-bottom: 15px;
            font-size: 1.4rem;
        }

        .level-card ul {
            list-style: none;
            margin-bottom: 20px;
        }

        .level-card ul li {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
            font-size: 0.95rem;
        }

        .price-tag {
            background-color: #eef7fc;
            padding: 12px;
            border-radius: 6px;
            text-align: center;
            font-weight: 700;
            color: var(--primary-color);
        }

        .grand-total-banner {
            background-color: var(--primary-color);
            color: var(--white);
            text-align: center;
            padding: 20px;
            border-radius: 8px;
            margin-top: 40px;
            font-size: 1.3rem;
            font-weight: 700;
        }

        /* قسم طرق الدفع */
        .payments-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .payment-box {
            background: var(--white);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            text-align: center;
            border: 1px solid #ddd;
        }

        .payment-box i {
            font-size: 2.5rem;
            color: var(--secondary-color);
            margin-bottom: 15px;
        }

        .payment-box h4 {
            color: var(--primary-color);
            margin-bottom: 10px;
        }

        .account-number {
            font-size: 1.2rem;
            font-weight: bold;
            color: #d90429;
            background: #fff0f3;
            padding: 8px;
            border-radius: 5px;
            margin-top: 10px;
            letter-spacing: 1px;
        }

        /* تذييل الصفحة (Footer) */
        footer {
            background-color: var(--primary-color);
            color: var(--white);
            text-align: center;
            padding: 30px 20px;
            margin-top: 60px;
        }

        footer p {
            margin-bottom: 10px;
        }

        .contact-info {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 15px;
            font-size: 1.1rem;
        }

        .contact-info a {
            color: var(--accent-color);
            text-decoration: none;
        }
    </style>
</head>
<body>

    <!-- رأس الصفحة وقائمة التنقل -->
    <header>
        <div class="navbar">
            <div class="logo-container">
                <div>
                    <h1>مكتب الحزمي</h1>
                    <span>لتحضير التوفل والآيلتس</span>
                </div>
            </div>
            <ul class="nav-links">
                <li><a href="#home">الرئيسية</a></li>
                <li><a href="#curriculum">خارطة الدورات</a></li>
                <li><a href="#payments">طرق الدفع</a></li>
                <li><a href="#contact">تواصل معنا</a></li>
            </ul>
            <a href="#payments" class="cta-btn">التسجيل الآن</a>
        </div>
    </header>

    <!-- الواجهة الترحيبية -->
    <section id="home" class="hero">
        <h2>معك نحو مستقبلك الأفضل</h2>
        <p>مرحباً بك في المنصة الرسمية لمكتب الحزمي. نقدم برامج احترافية شاملة ومدروسة بعناية للتحضير لاختباري التوفل والآيلتس وإتقان اللغة الإنجليزية من الصفر حتى الاحتراف.</p>
        <div class="hero-buttons">
            <a href="#curriculum" class="btn-light">استعراض المسار التعليمي</a>
        </div>
    </section>

    <!-- خارطة الدورات والمسار التعليمي -->
    <section id="curriculum" class="container">
        <h2 class="section-title">خارطة دورات اللغة الإنجليزية</h2>
        <div class="levels-grid">
            
            <!-- المستوى المبتدئ -->
            <div class="level-card">
                <h3>المستوى المبتدئ (Beginner)</h3>
                <ul>
                    <li>1. A1.1 - Beginner English 1</li>
                    <li>2. A1.2 - Beginner English 2</li>
                    <li>3. A2.1 - Elementary English 1</li>
                    <li>4. A2.2 - Elementary English 2</li>
                </ul>
                <p>عدد الدورات: 4 دورات (مدة كل دورة: شهر)</p>
                <div class="price-tag" style="margin-top: 15px;">
                    سعر الدورة: 5,000 ريال يمني قديم<br>
                    إجمالي المستوى: 20,000 ريال يمني قديم
                </div>
            </div>

            <!-- المستوى المتوسط -->
            <div class="level-card">
                <h3>المستوى المتوسط (Intermediate)</h3>
                <ul>
                    <li>5. B1.1 - Intermediate English 1</li>
                    <li>6. B1.2 - Intermediate English 2</li>
                    <li>7. B2.1 - Upper-Intermediate English 1</li>
                    <li>8. B2.2 - Upper-Intermediate English 2</li>
                </ul>
                <p>عدد الدورات: 4 دورات (مدة كل دورة: شهر)</p>
                <div class="price-tag" style="margin-top: 15px;">
                    سعر الدورة: 7,000 ريال يمني قديم<br>
                    إجمالي المستوى: 28,000 ريال يمني قديم
                </div>
            </div>

            <!-- المستوى المتقدم -->
            <div class="level-card">
                <h3>المستوى المتقدم (Advanced)</h3>
                <ul>
                    <li>9. C1.1 - Advanced English 1</li>
                    <li>10. C1.2 - Advanced English 2</li>
                    <li>11. C2.1 - Proficiency English 1</li>
                    <li>12. C2.2 - Proficiency English 2</li>
                </ul>
                <p>عدد الدورات: 4 دورات (مدة كل دورة: شهر)</p>
                <div class="price-tag" style="margin-top: 15px;">
                    سعر الدورة: 10,000 ريال يمني قديم<br>
                    إجمالي المستوى: 40,000 ريال يمني قديم
                </div>
            </div>

        </div>

        <div class="grand-total-banner">
            إجمالي البرنامج التدريبي الكامل: 12 دورة تدريبية — 88,000 ريال يمني قديم
        </div>
    </section>

    <!-- أرقام الحسابات وطرق الدفع -->
    <section id="payments" class="container" style="background-color: #fff; border-radius: 10px; margin-bottom: 40px;">
        <h2 class="section-title">أرقام حساباتنا وطرق الدفع</h2>
        <p style="text-align: center; margin-bottom: 30px;">لإيداع رسوم الدورات والاختبارات والخدمات. التسجيل مفتوح الآن: أرسل اسمك الرباعي في رسالة واتساب.</p>
        
        <div class="payments-grid">
            <div class="payment-box">
                <i class="fa-solid fa-wallet"></i>
                <h4>حساب وان كاش</h4>
                <p>مكتب الحزمي</p>
                <div class="account-number">151043060</div>
            </div>

            <div class="payment-box">
                <i class="fa-solid fa-building-columns"></i>
                <h4>حساب الكريمي صنعاء</h4>
                <p>مكتب الحزمي</p>
                <div class="account-number">3011338614</div>
            </div>

            <div class="payment-box">
                <i class="fa-solid fa-building-columns"></i>
                <h4>حساب الكريمي سعودي</h4>
                <p>مكتب الحزمي</p>
                <div class="account-number">3103563975</div>
            </div>

            <div class="payment-box">
                <i class="fa-solid fa-mobile-screen-button"></i>
                <h4>حساب محفظة جيب</h4>
                <p>مكتب الحزمي</p>
                <div class="account-number">733634356</div>
            </div>
        </div>
    </section>

    <!-- تذييل الصفحة -->
    <footer id="contact">
        <p>جميع الحقوق محفوظة © 2026 مكتب الحزمي لتحضير التوفل والآيلتس</p>
        <p>معاً نحو مستقبل مشرق</p>
        <div class="contact-info">
            <a href="https://wa.me/967782404521" target="_blank"><i class="fa-brands fa-whatsapp"></i> +967 782 404 521</a>
            <a href="https://wa.me/967739913814" target="_blank"><i class="fa-brands fa-whatsapp"></i> +967 739 913 814</a>
        </div>
    </footer>

</body>
</html>
