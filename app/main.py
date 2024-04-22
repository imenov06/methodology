from app.methodologies.repo import MethodologiesRepo
from database.core import Core


def main():
    Core.create_tables()
    Core.insert_test_data()

    a = MethodologiesRepo.join_method_images(1)
    print(a)



if __name__ == '__main__':
    main()
