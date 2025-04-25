<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abel - Software Developer Portfolio</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      color: #000;
      background-color: #ffffff;
    }
    header, section, footer {
      padding: 60px 30px;
    }
    header {
      background-color: #000;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      color: white;
    }
    header h1 {
      font-size: 3rem;
      color: orange;
    }
    .intro p {
      max-width: 600px;
      font-size: 1.2rem;
      color: white;
    }
    .profile-pic {
      width: 180px;
      height: 180px;
      border-radius: 50%;
      object-fit: cover;
      border: 4px solid orange;
      margin-left: 20px;
    }
    .recent-works, .about-me, .contact {
      border-radius: 12px;
      margin: 20px;
      padding: 40px;
    }
    .recent-works {
      background: rgba(255, 255, 255, 0.9);
    }
    .section-title {
      font-size: 2rem;
      color: orange;
      margin-bottom: 20px;
      border-bottom: 2px solid orange;
      display: inline-block;
    }
    .about-me {
      background-color: black;
      color: orange;
    }
    .contact {
      background-color: white;
      color: orange;
    }
    .contact-form input, .contact-form textarea {
      width: 100%;
      padding: 12px;
      margin-top: 10px;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid #ccc;
      color: orange;
      border-radius: 8px;
    }
    .contact-form input::placeholder,
    .contact-form textarea::placeholder {
      color: #999;
    }
    .btn {
      background: orange;
      color: #000;
      border: none;
      padding: 12px 25px;
      cursor: pointer;
      margin-top: 10px;
      font-weight: bold;
      border-radius: 8px;
      transition: background 0.3s ease;
    }
    .btn:hover {
      background: darkorange;
    }
    .contact-links a {
      color: orange;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: bold;
      transition: color 0.3s ease;
    }
    .contact-links a:hover {
      color: black;
    }
    .tag {
      display: inline-block;
      background: #ffe0b2;
      color: orange;
      padding: 3px 10px;
      margin-right: 5px;
      font-size: 0.75rem;
      border-radius: 4px;
    }
    .project-card img {
      width: 100%;
      height: 250px;
      object-fit: cover;
    }
    .overlay {
      background: linear-gradient(0deg, rgba(0,0,0,0.6), rgba(0,0,0,0.1));
      color: white;
      padding: 1rem;
    }
    .carousel {
      overflow: hidden;
    }
    .carousel-track {
      display: flex;
      animation: scroll 15s linear infinite;
      gap: 1rem;
    }
    @keyframes scroll {
      from { transform: translateX(0); }
      to { transform: translateX(-100%); }
    }
  </style>
</head>
<body>
  <header>
    <div class="intro">
      <h1>Hey There. <br>I'm Abel.</h1>
      <p>I'm a passionate ITS student and an aspiring software developer. I also play soccer for a youth team, where I’ve learned the value of teamwork, discipline, and pushing boundaries—skills I bring to the tech world as well.</p>
    </div>
    <div>
      <img src="abela2.jpg" alt="Abel's Photo" class="profile-pic">
    </div>
  </header>

  <section class="recent-works">
    <h2 class="section-title">My Recent Works</h2>
    <div class="carousel">
      <div class="carousel-track">
        <div class="card project-card" style="min-width: 300px;">
          <img src="https://via.placeholder.com/300x200?text=Game+1" alt="Soccer Quote 1">
          <div class="overlay">
            <h5>"We gave it 110% out there"</h5>
            <p>Every game is a battle, and we’re always pushing past the limit. That’s how champions are made.</p>
            <div><span class="tag">HTML</span><span class="tag">Bootstrap</span><span class="tag">Ruby</span></div>
          </div>
        </div>

        <div class="card project-card" style="min-width: 300px;">
          <img src="https://via.placeholder.com/300x200?text=Game+2" alt="Soccer Quote 2">
          <div class="overlay">
            <h5>"It's not over till the final whistle"</h5>
            <p>No matter the score, we fight to the end. Passion, grit, and teamwork—that’s the beautiful game.</p>
            <div><span class="tag">HTML</span><span class="tag">Bootstrap</span><span class="tag">Ruby</span></div>
          </div>
        </div>

        <div class="card project-card" style="min-width: 300px;">
          <img src="https://via.placeholder.com/300x200?text=Game+3" alt="Soccer Quote 3">
          <div class="overlay">
            <h5>"We play for the badge on the front"</h5>
            <p>And they’ll remember the name on the back. Loyalty and pride in every match we play.</p>
            <div><span class="tag">HTML</span><span class="tag">Bootstrap</span><span class="tag">Ruby</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="about-me">
    <h2 class="section-title">About Me</h2>
    <p>Hi! I'm Abel, an Information Technology and Systems student with a drive to innovate and build useful, modern web applications. I combine my passion for technology with the strategic mindset I’ve developed as a youth team soccer player. My interests range from web development and database design to exploring how technology can create real impact in education, sports, and communities. I am continually learning, collaborating, and striving to build better digital experiences.</p>
    <div class="grid">
      <div><strong>acolades</strong><br>Gold medal, golden boot, junior puskas</div>
      <div><strong>talents</strong><br>musican, track and feild, acting</div>
      <div><strong>Skills</strong><br>Elastico, Around the world, Rabona</div>
    </div>
  </section>

  <section class="contact">
    <h2 class="section-title">Get In Touch</h2>
    <p>I'm always interested in hearing about new projects. Drop a message below!</p>

    <div class="contact-links">
      <a href="mailto:abel.mulu@bitscollege.edu.et"><i class="fas fa-envelope"></i> abel.mulu@bitscollege.ed.et</a>
      <a href="https://www.instagram.com/abel_m07" target="_blank"><i class="fab fa-instagram"></i> @abel_m07</a>
    </div>

    <form class="contact-form">
      <input type="text" name="name" placeholder="First Name">
      <input type="text" name="lastname" placeholder="Last Name">
      <textarea name="message" placeholder="Share your thoughts..."></textarea>
      <button type="submit" class="btn">Send Message</button>
    </form>
  </section>

  <footer>
    <p>&copy; 2025 Abel. All rights reserved.</p>
  </footer>
</body>
</html>
