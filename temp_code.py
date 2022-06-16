class YourBot(BaseBot):
    def _roll_bank_or_quit(self):

        """your logic here"""
        self.print_all = True
        if self.dice_remaining >= 3:
            return 'r'

        return 'b'






    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        # if 1 in self.last_roll:
        #     print('true')
        roll = GameLogic.get_scorers(self.last_roll)
        roll_list = list(roll)
        new_list_ones  = [index for (index, item) in enumerate(self.last_roll) if item == 1]
        new_list_twos  = [index for (index, item) in enumerate(self.last_roll) if item == 2]
        new_list_threes  = [index for (index, item) in enumerate(self.last_roll) if item == 3]
        new_list_fours  = [index for (index, item) in enumerate(self.last_roll) if item == 4]
        new_list_fives  = [index for (index, item) in enumerate(self.last_roll) if item == 5]
        print(str(new_list_fives))
        new_list_sixes  = [index for (index, item) in enumerate(self.last_roll) if item == 6]


        if new_list_ones:
            if not self.dice_remaining or self.dice_remaining >= 4:
                roll_list.sort()
                self.report("> " + (str(roll_list[0])))
                roll_list = str(roll_list[0])
                return roll_list
            else:
                roll_list.sort()
                if len(roll_list) >= 2:
                    list_of_ones = ''
                    for num in roll_list:
                        list_of_ones += str(num)
                    self.report("> " + list_of_ones)
                    roll_list = str(roll_list)
                    return roll_list
        elif new_list_fives:
            if not self.dice_remaining or self.dice_remaining >= 4:
                if not new_list_ones:
                    roll_list.sort()
                    self.report("> " + (str(roll_list[0])))
                    roll_list = str(roll_list[0])
                    return roll_list
            else:
                roll_list.sort()
                # if len(roll_list) <= 2:
                list_of_fives = ''
                for num in roll_list:
                    list_of_fives += str(num)
                self.report("> " + list_of_fives)
                roll_list = str(roll_list)
                return roll_list
        return 'r'

        # return super()._enter_dice()
