@app.post("/screen")
async def screen_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    file_path = UPLOAD_DIR / resume.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    if resume.filename.lower().endswith(".pdf"):
        resume_text = extract_text_from_pdf(str(file_path))

    elif resume.filename.lower().endswith(".txt"):
        resume_text = extract_text_from_txt(str(file_path))

    else:
        return {
            "error": "Only PDF and TXT files are supported"
        }

    resume_data = analyze_resume(resume_text)

    match_data = match_resume(
        resume_text,
        job_description
    )

    candidate = Candidate(
        name=resume_data.get("name", "Unknown"),
        email=resume_data.get("email"),
        resume_text=resume_text,
        skills=json.dumps(resume_data.get("skills", [])),
        experience=resume_data.get("experience", ""),
        education=resume_data.get("education", ""),
        match_score=match_data.get("score"),
        matching_skills=json.dumps(
            match_data.get("matching_skills", [])
        ),
        missing_skills=json.dumps(
            match_data.get("missing_skills", [])
        ),
        justification=match_data.get("justification")
    )

    with Session(engine) as session:
        session.add(candidate)
        session.commit()
        session.refresh(candidate)

    return {
        "candidate_id": candidate.id,
        "candidate": resume_data,
        "match": match_data
    }
