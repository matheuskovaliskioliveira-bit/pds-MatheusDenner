from app import app, db, Dono, Pet

with app.app_context():
    db.create_all()

    # Só adiciona os dados se o banco estiver vazio
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

        db.session.add(ana)
        db.session.add(bruno)
        db.session.add(carla)

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

        nina = Pet(
            nome="Nina",
            especie="gato",
            idade=1,
            dono_id=carla.id
        )

        pingo = Pet(
            nome="Pingo",
            especie="passaro",
            idade=3,
            dono_id=carla.id
        )

        db.session.add(rex)
        db.session.add(mimi)
        db.session.add(thor)
        db.session.add(nina)
        db.session.add(pingo)

        db.session.commit()

    print("Banco criado com sucesso.")
