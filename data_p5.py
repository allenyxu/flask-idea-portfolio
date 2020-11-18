"""Data file for Period 1"""

import model  # projects definitions are placed in different file
from flask import url_for


def setup():
    EXAMPLE = model.Project("Example", url_for('teacher_bp.index'), "/static/img/teacher.png", "Team Teacher",
                            ["John Mortensen", "Classroom of 40"],
                            "Visit a VANTA birds experience and see how it is made.")

    p5_calculus = model.Project("p5_calculus", "https://github.com/AkhileshLG/flaskportfolio-1",
                                "/static/img/AkaTeamCalculus.png", "calculus",
                                ["Karam Alshaikh", "Akhilesh Genneri", "Akshit Prathipati", "Noya Hafiz",
                                 "Jien (Max) Wang"],
                                "This website is used for everything calculus and to spread our information about it")

    p5_chessGame = model.Project("Chess Game", url_for('p5_chessGame_bp.index'),
                                "/static/img/p5chessGame.JPG", "Chess Game",
                                ["Colin Szeto", "Devam Shrivastava", "Shekar Krishnamoorthy", "Kyle Myint",
                                 "David Kim"],
                                "Vist Chess Game to play through our chess game!")

    projects = [p5_calculus, p5_chessGame, EXAMPLE]
    period = model.Period("Period 5", "Some really smart people study apcsp here", projects)
    return period
