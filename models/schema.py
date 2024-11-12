from typing import List, Optional

from pydantic import BaseModel


class EducationDetail(BaseModel):
    institution_name: Optional[str] = None
    degree_name: Optional[str] = None
    graduation_date: Optional[str] = None


class WorkExperience(BaseModel):
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    duration: Optional[str] = None
    responsibilities: Optional[str] = None


class AutomaticExtractionModel(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    education_details: Optional[List[EducationDetail]] = None
    work_experience: Optional[List[WorkExperience]] = None
    skills: Optional[List[str]] = None
    certifications: Optional[List[str]] = None
