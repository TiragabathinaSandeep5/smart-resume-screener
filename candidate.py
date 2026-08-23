@app.get("/candidates")
def get_candidates():

    with Session(engine) as session:

        candidates = session.exec(
            select(Candidate)
            .order_by(Candidate.match_score.desc())
        ).all()

        return candidates
