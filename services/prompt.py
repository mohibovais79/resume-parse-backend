def return_prompt(resume_text: str):
    prompt = f"You are an expert resume reader and here is the  provided resume text {resume_text} from which you are required to extract following fields and return answer in json format.Here are the required fields name,email,phone,address,education details (Note: For Education detail format will be institution name,degree name,graduation date. No other text except this), work experience (Note: For work experience format will be company name, job title, duration,responsibilities. No other text except this),skills,certifications"
    return prompt
