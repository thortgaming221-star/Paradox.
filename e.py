
import turtle
import streamlit as st
import time
import pandas as pd
import smtplib
from smtplib import EmailMessage

st.title("Welcome to PARADOX" )
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.pexels.com/photos/24862895/pexels-photo-24862895/free-photo-of-people-paddleboarding-in-a-green-scenic-lake.jpeg?auto=compress&w=1260&h=750&dpr=1");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)
name = st.text_input("Enter your name" )
button = st.button("Submit")
if button:
        with st.spinner("Processing..."):
              time.sleep(2)
              st.write(f"Hello, {name}! Welcome to PARADOX.")

              st.title("📊 My First Chart")

              data = pd.DataFrame({
                  "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                  "Python": [10, 25, 20, 40, 35],
                  "Gaming": [15, 20, 30, 25, 45]
              })
              
              data = data.set_index("Day")
              
              st.line_chart(data)
              turtle.pendown()

              data = pd.DataFrame({
                    "Category": ["A-growth 72%", "B-share hodler 25%", "C-others 3%"],
                  "Value": [72, 25, 3]
              })
              st.title("Circle Chart")
              st.vega_lite_chart(data, {
                    "mark": {"type": "arc"},
                  "encoding": {
                        "theta": {"field": "Value", "type": "quantitative"},
                      "color": {"field": "Category", "type": "nominal"}
                  }
              })
              
              st.subheader("My Company Branches")
              table = pd.DataFrame ({
                 "Branches":[
                 "Eiffel Tower — France",
                 "Statue of Liberty — USA",
                 "Great Wall of China — China",
                 "Burj Khalifa — UAE",
                 "Big Ben — UK",
                 ],
                 "Main branches": [
                        "Pyramids of Giza — Egypt",
                        "Sydney Opera House — Australia",
                        "Christ the Redeemer — Brazil",
                        "Mount Fuji — Japan",
                        None,
                        ],
                        
             })


st.markdown("""

# 🌟 About Me – Pranav Kumar Singh (Founder and chair man) 🚀

## 👋 Introduction

Hello everyone! 😊 My name is **Pranav Kumar Singh**. I am a student who is curious, creative, and passionate about learning new things. 🌟 I believe that knowledge is one of the most powerful tools in the world, and I always try to improve myself by learning something new every day. 📚 I enjoy exploring technology, discovering new ideas, solving problems, and turning my imagination into reality. 💡

I am especially interested in computers, programming, artificial intelligence, website development, and game development. 💻 My dream is to become a skilled developer who can create useful, creative, and innovative projects that make people's lives easier. 🚀

## 💻 My Interest in Technology

Technology is one of my biggest interests. 🌐 I love learning how computers work, how websites are created, how applications function, and how software can solve real-world problems.

Whenever I discover something new about technology, I become excited to understand how it works. 🔍 I enjoy experimenting with different tools, exploring new programming techniques, and finding creative ways to build projects.

I believe technology offers endless opportunities for learning and creativity. 🌍 In the future, I want to explore advanced technologies and use my knowledge to create projects that are both interesting and helpful.

## 🐍 My Programming Journey

Python is one of the programming languages I enjoy learning. 🐍 I like Python because its syntax is easy to understand, and it allows beginners to create many different types of projects.

I am interested in learning how to use variables, loops, conditions, functions, modules, and libraries. 🧠 These concepts help me understand the logic behind computer programs.

I also enjoy experimenting with Python projects, including simple games, calculators, interactive applications, and other creative programs. 🎮 Every project gives me an opportunity to learn something new and improve my problem-solving skills.

My goal is to become confident in programming and gradually develop more advanced applications. 🚀 I understand that learning to code requires patience, practice, and consistency, so I want to keep improving step by step.

## 🌐 My Interest in Web Development

Website development is another area that fascinates me. 🌐 I enjoy learning how websites are designed, how their layouts are created, and how users interact with different elements.

I am interested in **HTML, CSS, JavaScript, Python, and Streamlit**. 🛠️ Each technology has its own purpose in building websites and web applications.

HTML helps structure web pages, CSS makes them visually attractive, and JavaScript adds interactive features. Python and Streamlit allow me to create useful web applications using Python code.

I want to learn how to build personal portfolios, interactive dashboards, educational websites, gaming websites, and other exciting projects. 🎨 My aim is to create websites that are attractive, easy to use, and useful for visitors.

## 🎮 My Passion for Game Development

Games are another source of inspiration for me. 🕹️ I enjoy exploring games, understanding their mechanics, and thinking about how they are developed.

Game development combines programming, creativity, logical thinking, and design. 🎯 This makes it an exciting field for someone who enjoys both technology and imagination.

I am interested in creating games using Python and exploring different game development tools. I would love to develop racing games, adventure games, puzzle games, and other interactive experiences. 🏎️

I also enjoy Minecraft Pocket Edition because it offers opportunities for creativity, exploration, and building. ⛏️ Creating structures, exploring different environments, and discovering new ideas make gaming enjoyable for me.

In the future, I hope to develop my own games and share them with other people. 🌟

## 🤖 My Interest in Artificial Intelligence

Artificial intelligence, commonly known as AI, is one of the most exciting areas of modern technology. 🤖 I am interested in understanding how AI systems learn, process information, recognize patterns, and help people complete different tasks.

AI has many applications, including education, science, programming, communication, and creative work. 🌍 I want to learn how artificial intelligence can be used responsibly to solve problems and improve everyday life.

I am also interested in exploring AI-powered applications and understanding how they are built. 💡 As my programming knowledge grows, I hope to create simple intelligent tools and experiment with machine learning.

I believe that learning about AI can help me understand the future of technology and discover new opportunities.

## 🧠 My Problem-Solving Skills

I enjoy solving challenging problems because they help me develop logical thinking and patience. 🧩 Whether I am working on a mathematics question, debugging a Python program, or planning a website, I try to understand the problem before finding a solution.

Programming teaches me that mistakes are a natural part of learning. 🔧 Sometimes a program does not work as expected, but examining the error can help me understand the code better.

I believe that every challenge provides an opportunity to learn something valuable. 💪 Instead of giving up immediately, I want to develop the habit of trying different approaches and learning from my mistakes.

## 📚 My Learning Philosophy

I believe learning should never stop. 📖 The world is constantly changing, and new technologies are being developed every day.

I want to build a strong foundation in mathematics, science, computer science, and communication. 🎓 These subjects can help me become a better student and a more capable developer.

I also believe that practical experience is important. Building projects, testing ideas, reading documentation, and practicing regularly can help turn theoretical knowledge into real skills. 🛠️

My learning philosophy is simple: start with the basics, practice consistently, ask questions, and gradually take on more challenging tasks. 🚀

## 🎨 My Creativity and Imagination

Creativity is an important part of my personality. ✨ I enjoy thinking about new ideas and imagining how they could become real projects.

Sometimes an idea begins as a simple thought, but with planning, learning, and effort, it can develop into something useful. 💡 This is one reason I enjoy programming and website development.

I like experimenting with designs, choosing colors, organizing layouts, and thinking about how to make digital projects more interesting. 🎨 I want my work to reflect both logical thinking and creative imagination.

## 🏆 My Goals and Dreams

Everyone needs goals to guide their journey, and I have many things I want to achieve. 🌟 My main goal is to become a knowledgeable and skilled developer.

I want to improve my Python programming, master web development fundamentals, explore artificial intelligence, and learn more about game development. 💻

I also want to build a collection of original projects that demonstrate my creativity and technical skills. 🚀 These projects could include websites, games, interactive dashboards, educational tools, and useful applications.

Another goal is to develop confidence in sharing my work with others. 🌐 I hope to learn how to explain my projects clearly, accept constructive feedback, and collaborate with people who share similar interests.

I understand that success does not happen overnight. It requires dedication, discipline, curiosity, and consistent effort. 💪 I am willing to keep learning and improving as I work toward my dreams.

## 🌈 My Values

I believe in honesty, respect, creativity, and hard work. ❤️ I want to treat other people respectfully and remain open to learning from their experiences.

I also believe that helping others is important. 🤝 Knowledge becomes more valuable when we use it to solve problems, share ideas, and support people around us.

When working with technology, I want to follow responsible practices, respect privacy, and use my programming skills for constructive purposes. 🔐 I believe that developers should think carefully about how their creations affect other people.

## 🌍 My Vision for the Future

When I think about the future, I imagine myself creating innovative software, developing exciting games, building modern websites, and exploring advanced technologies. 🚀

I want to understand not only how to write code but also how to design effective solutions to real problems.

I hope to continue learning new programming languages, exploring useful tools, and developing projects that reflect my interests. 🌟 Every new skill I learn can bring me one step closer to my goals.

I know that the journey may include difficulties, mistakes, and unexpected challenges. However, I believe that patience and consistent effort can help me overcome obstacles and grow as a person.

## 🙏 Final Words

Thank you for visiting my personal introduction! 😊 I am **Pranav Kumar Singh**, a student, a technology enthusiast, a creative thinker, and an aspiring developer. 💻

I enjoy learning Python, exploring web development, experimenting with game development, and discovering the possibilities of artificial intelligence. 🤖 I want to keep improving my skills, building interesting projects, and turning my ideas into reality.

My journey is still beginning, and there is a lot more for me to learn and explore. 📚 I believe every small step matters, every mistake teaches a lesson, and every new idea creates an opportunity.

**Keep learning, keep creating, keep exploring, and never stop dreaming!** 🌟🚀💻

Shorten my introduction for clarityReduce repeated ideas across sections""")


feedback = st.text_input("Enter your feedback here")
k = st.button("Submit.")

if feedback:
    with st.spinner("Processing..."):
          time.sleep(2)
          st.write(f"Thankyou for your feedback." , name)
          



# st.subheader("\nsend message on thortgaming@gmail.com") 