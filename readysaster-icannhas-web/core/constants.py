from model_utils import Choices


CHOICES = {
    # Samples only. More can be added later
    'HAZARD': Choices(
        (1, 'flooding', 'Flooding'),
        (2, 'severe_wind', 'Severe Wind'),
        (3, 'landslide', 'Landslide'),
        (4, 'storm_surge', 'Storm Surge'),
    ),

    'EVENT': Choices(
        (1, 'heavy_rainfall', 'Rainfall'),
        (2, 'typhoon', 'Typhoon')
    ),

    # taken from PAGASA's 3-color rainfall warning
    'RAINFALL_WARNING': Choices(
        (0, 'none', ''),
        (1, 'heavy', 'Heavy'),
        (2, 'intense', 'Intense'),
        (3, 'torrential', 'Torrential')
    )
}

# CHOICES_VERBOSE_NAMES = {k: dict(v._choices) for k, v in CHOICES.iteritems()}
