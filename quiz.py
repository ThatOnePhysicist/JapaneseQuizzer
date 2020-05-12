class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "?\n(a) Red/Green\n(b)Orange",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow",
]
for loop questions
for i in range(0,46):
    return Question(question_prompts[i])
print(Question)

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)
