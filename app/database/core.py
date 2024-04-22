from sqlalchemy import text

from app.database.db_connect import engine, Base, session_maker
from app.methodologies.models import Methodologies, ImagesInMethodologies


class Core:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_test_data():
        with session_maker() as session:
            query = text("""
                INSERT INTO methodologies (id, title, description,  is_published,avatar_url) VALUES 
                (1, 'Метод 1','Описание', True,'https://c.dns-shop.ru/thumb/st1/fit/500/500/5abe99cf75ba30dfbf5d3df0e51fcd2e/8c13db2ae30d4a80ff48b0d28a21fc90fe87c7e9646453fa6ba432d049e5334a.jpg.webp' ),
                (2, 'Метод 2','Описание', True,'https://c.dns-shop.ru/thumb/st1/fit/500/500/5abe99cf75ba30dfbf5d3df0e51fcd2e/8c13db2ae30d4a80ff48b0d28a21fc90fe87c7e9646453fa6ba432d049e5334a.jpg.webp' ),
                (3, 'Метод 3','Описание', True,'https://c.dns-shop.ru/thumb/st1/fit/500/500/5abe99cf75ba30dfbf5d3df0e51fcd2e/8c13db2ae30d4a80ff48b0d28a21fc90fe87c7e9646453fa6ba432d049e5334a.jpg.webp' ),
                (4, 'Метод 4','Описание', True,'https://c.dns-shop.ru/thumb/st1/fit/500/500/5abe99cf75ba30dfbf5d3df0e51fcd2e/8c13db2ae30d4a80ff48b0d28a21fc90fe87c7e9646453fa6ba432d049e5334a.jpg.webp' );
                
                INSERT INTO images (id,method_id, url) VALUES 
                (1,1,'https://c.dns-shop.ru/thumb/st4/fit/500/500/1282a823385e8f03a3611299a5c5ed6f/f0829893e28b9a0d2f5c18937c1911c2c9f24beb32a25c81570de7916c2f9db9.jpg.webp'),
                (2,1,'https://c.dns-shop.ru/thumb/st1/fit/wm/0/0/6fd87ae734abecd11b07ec163bad71db/962092c6b8e170a3373085b13837c38114c0399b95aada8428af57e93cdaf0e0.jpg.webp'),
                (3,2,'https://c.dns-shop.ru/thumb/st1/fit/wm/0/0/6fd87ae734abecd11b07ec163bad71db/962092c6b8e170a3373085b13837c38114c0399b95aada8428af57e93cdaf0e0.jpg.webp');
                
                
                        """)

            session.execute(query)
            session.commit()
