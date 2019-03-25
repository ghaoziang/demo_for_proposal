import yaml


class Unit:
    def __init__(self, unit_id, field_file, field_list=None, last_field=None):
        self._unit_id = unit_id
        self._field_file = field_file
        self._field_list = field_list
        self._last_field = last_field
        self._current_field = dict()
        self.read_field_file()

    @property
    def unit_id(self):
        return self._unit_id

    @property
    def field_file(self):
        return self._field_file

    @property
    def field_list(self):
        return self._field_list

    """the target unit observed at the last time"""
    @property
    def last_field(self):
        return self._last_field

    """the target unit observe now"""
    @property
    def current_field(self):
        return self._current_field

    @field_list.getter
    def get_field_list(self):
        return self._field_list

    def set_last_field(self, field):
        self._last_field = field

    def set_current_field(self, field):
        self._last_field = self._current_field
        self._current_field = field

    def read_field_file(self):
        if self._field_file is not None:
            with open(self._field_file, 'r') as f:
                self._field_list = yaml.load(f.read())

