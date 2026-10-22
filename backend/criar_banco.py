
from app import app, db, Dono, Pet

with app.app_context():

    db.create_all()

    if Dono.query.first() is None:

        ana = Dono(
            nome="Ana Paula Ribeiro",
            telefone="45999110001"
        )

        bruno = Dono(
            nome="Bruno Cardoso",
            telefone="45999110002"
        )

        carla = Dono(
            nome="Carla Meneghel",
            telefone="45999110003"
        )

        db.session.add_all([ana, bruno, carla])
        db.session.commit()

        rex = Pet(
            nome="Rex",
            especie="cachorro",
            idade=4,
            dono_id=ana.id
        )

        mimi = Pet(
            nome="Mimi",
            especie="gato",
            idade=2,
            dono_id=ana.id
        )

        thor = Pet(
            nome="Thor",
            especie="cachorro",
            idade=7,
            dono_id=bruno.id
        )

        mel = Pet(
            nome="Mel",
            especie="gato",
            idade=3,
            dono_id=bruno.id
        )

        bidu = Pet(
            nome="Bidu",
            especie="cachorro",
            idade=1,
            dono_id=ana.id
        )

        db.session.add_all([
            rex,
            mimi,
            thor,
            mel,
            bidu
        ])

        db.session.commit()

        print("Banco criado e populado com sucesso!")

    else:
        print("Banco ja possui dados.")
