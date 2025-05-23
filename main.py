from PyPDF2 import PdfReader
import google.generativeai as genai

genai.configure(api_key="AIzaSyCE_iYZEKcioMkRBCIFy6_CoxyakGaQN0Y")

def reading(location,Start_page_number,End_page_number):
    reader = PdfReader(location)
    text = ""
    for i in range(Start_page_number-1,End_page_number):
        page = reader.pages[i]
        text = text + "\n" + page.extract_text()
    return text

def command_to_gemini(prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
        reply = response.text.strip() if response.text else "Sorry, I didn't get an answer."
        return reply
        
    except Exception as e:
        print(f"Sorry I couldn't generate the questions because of {e}")    
        

if( __name__ == "__main__"):
    print("Let me help you to find Questions from your PDF")
    
    pdf_file_location = input("Give me the location of the PDF: ")
    
    Starting_page = int(input("Enter The page Number from where you want to start: "))
    Ending_page = int(input("Enter The Ending Page Number: "))
    
    text = reading(pdf_file_location,Starting_page,Ending_page)
    
    NO_questions = int(input("How much questions you want to generate? \n"))
    
    Toughness = input("And What kind of toughness are you prefer \nEasy \nModerate \nHard \n")
    
    Final_text = f"I’ll give you a text below. From that, please create {NO_questions} {Toughness}-level questions  Only Questions Not any other word than questions.. that cover the important points, ideas, or facts in the passage.Focus on comprehension, not just surface-level facts. " + text
    
    questions = command_to_gemini(Final_text)
    print("\n",questions)
    
    ask_for_answers = input("\n-----------Do you want answers?-----------\n")
    if(ask_for_answers.lower() == "yes"):
        prompt_for_answers = "Please give me the answers of the Following Questions from the following text With numbers as bullets Without repeating the questions only answers." +"\n" + text +"\n"+ questions
        print(command_to_gemini(prompt_for_answers))        
