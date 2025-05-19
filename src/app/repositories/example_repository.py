from sqlalchemy.orm import Session

class ExampleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_example(self, example_id: int):
        # Replace with actual database query logic
        return self.db.query().filter_by(id=example_id).first()

    def create_example(self, example_data):
        # Replace with actual database insert logic
        self.db.add(example_data)
        self.db.commit()
        self.db.refresh(example_data)
        return example_data

    def update_example(self, example_id: int, updated_data):
        # Replace with actual database update logic
        example = self.get_example(example_id)
        if example:
            for key, value in updated_data.items():
                setattr(example, key, value)
            self.db.commit()
            self.db.refresh(example)
        return example

    def delete_example(self, example_id: int):
        # Replace with actual database delete logic
        example = self.get_example(example_id)
        if example:
            self.db.delete(example)
            self.db.commit()
        return example