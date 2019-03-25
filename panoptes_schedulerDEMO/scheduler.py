
import random


class Scheduler:

    def __init__(self, unit_list, sorted_list=None, best_option=None):
        self._unit_list = unit_list
        self._sorted_list = sorted_list
        self._best_option = best_option

    """unit lists to store site info"""
    @property
    def unit_list(self):
        return self._unit_list

    """current best target for the pointed unit"""
    @property
    def best_option(self):
        return self._best_option

    """
    The demo hasn't added constraint functions to evaluate scores of the field, so I replace with random scores.
    """
    def add_score(self, unit_id):
        field_list = self._unit_list[unit_id].get_field_list
        for i in range(len(self._unit_list[unit_id].get_field_list)):
            field_list[i]['priority'] = field_list[i]['priority'] + random.randint(0, 200)

    """
    This method is only responsible for returning a target list file without any constraints
    """
    def read_best_option(self, unit_id):
        self.add_score(unit_id)
        """sort the field list and pick the first element as the best target"""
        self._sorted_list = sorted(self._unit_list[unit_id].get_field_list, key=lambda field: field['priority'], reverse=True)
        index = 0
        for i in range(len(self._unit_list)):
            if self._unit_list[i].current_field.get('name') == self._sorted_list[index].get('name'):
                index += 1
        self._best_option = self._sorted_list[index]
        self._unit_list[unit_id].set_current_field(self._best_option)

    """
    Schedule units with specific target, this is for incorporate multiple units to observe one target sequentially
    """
    def read_specific_option(self, unit_id, target):
        field_list = self._unit_list[unit_id].get_field_list

        """locate the position of target in the field list. If it does not exist, do simple target algorithm"""
        index = -1
        in_list = False
        for i in range(len(field_list)):
            if target == field_list[i].get('name'):
                index = i
                in_list = True
                break

        if in_list is False:
            self.read_best_option(unit_id)
            return

        """if the unit observed the target now, it will do simple target algorithm"""
        if target == self._unit_list[unit_id].current_field:
            self.read_best_option(unit_id)
            return

        """
        Test if there is any unit observe the target at the last observation.If there is, pick the target element.
        Thus, it is sequentially observing the target
        """
        valid = False
        for i in range(len(self._unit_list)):
            if target == self._unit_list[i].last_field:
                valid = True
                break

        if valid is True:
            self._best_option = field_list[index]
            self._unit_list[unit_id].set_current_field(self._best_option)
        else:
            """
            if there is no unit observe the target at the last observation, 
            check if other units observe the target now
            """
            is_beginning = True
            for i in range(len(self._unit_list)):
                if target == self._unit_list[i].current_field.get('name'):
                    is_beginning = False

            if is_beginning is True:
                """
                if there is no unit observing the target now, pick the target option 
                as it may be the beginning of the sequential observation
                """
                self._best_option = field_list[index]
                self._unit_list[unit_id].set_current_field(self._best_option)
            else:
                """
                if there is at least one unit observing the target now, 
                doing simple target algorithm to avoid observing same targets
                """
                self.read_best_option(unit_id)
