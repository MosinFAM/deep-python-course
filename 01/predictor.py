class SomeModel:
    def predict(self, message: str) -> float:
        return 1


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    prediction = model.predict(message)
    if prediction > 1 or prediction < 0:
        raise ValueError('Недопустимое значение')
    elif bad_thresholds >= good_thresholds:
        raise ValueError('Недопустимое значение')
    else:
        if prediction < bad_thresholds:
            return "неуд"
        if bad_thresholds <= prediction <= good_thresholds:
            return "норм"
        if prediction > good_thresholds:
            return "отл"
