format={
    "type": "json_schema",
    "json_schema": {
        "name": "ResumeExtraction",
        "schema": {
            "title": "ResumeExtraction",
            "description": "Extracted information from resume",
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The full name of the person from the resume."
                },
                "email": {
                    "type": "string",
                    "description": "The email address of the person from the resume."
                },
                "phone": {
                    "type": "string",
                    "description": "The phone number from the resume."
                },
                "address": {
                    "type": "string",
                    "description": "The physical address of the person from the resume.",
                },
                "education_details": {
                    "type": "array",
                    "description": "List of educational qualifications.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "institution_name": {
                                "type": "string"
                            },
                            "degree_name": {
                                "type": "string"
                            },
                            "graduation_date": {
                                "type": "string",
                                "format": "date"
                            },
                        },
                        "required": [
                            "institution_name",
                            "degree_name",
                            "graduation_date"
                        ],
                    },
                },
                "work_experience": {
                    "type": "array",
                    "description": "List of past job experiences.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "company_name": {
                                "type": "string"
                            },
                            "job_title": {
                                "type": "string"
                            },
                            "duration": {
                                "type": "string"
                            },
                            "responsibilities": {
                                "type": "string"
                            },
                        },
                        "required": [
                            "company_name",
                            "job_title",
                            "duration",
                            "responsibilities"
                        ],
                    },
                },
                "skills": {
                    "type": "array",
                    "description": "List of skills the person has.",
                    "items": {
                        "type": "string"
                    },
                },
                "certifications": {
                    "type": "array",
                    "description": "List of certifications obtained by the person.",
                    "items": {
                        "type": "string"
                    },
                },
            },
            "required": [
                "name",
                "email",
                "phone"
            ],
            "additionalProperties": False,
        },
    },
}