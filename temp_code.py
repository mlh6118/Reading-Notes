# 0. Check for and bank:
# 0A. Straight
# 0B. Three pairs
# 0C. Two sets of 3 of a kind.
# 1. Check for 3 or more of a kind.
# 2. If 3 or more of a kind are anything but 2s, keep the multiples.
# 3. Keep all 1s and 5s.
# 4. Bank points.
# 5. If no multiples of 3 or more (other than 2s), check how many dice are remaining to roll.
# 6. If dice remaining to roll are more than 3 or has no value due to start of round:
# 6A. Check for a 1.
# 6B. Save a single 1, if found.
# 6C. If no 1, check for a 5.
# 6D. Save a single 5, if found.
# 7. Roll remaining dice.


class YourBot(BaseBot):

    def __init__(self):
        from collections import Counter

    def _roll_bank_or_quit(self):

        """your logic here"""
        self.print_all = True
        if self.dice_remaining >= 3:
            return 'r'

        return 'b'

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        count = Counter(roll).most_common()
#        num = len(count) # not needed?

        # Check if roll is a straight.
        if len(count) == 6:
            return 'b'
        # Check if roll is two sets of triples.
        elif len(count) == 2:
            if count[0][1] == 3:
                return 'b'
        # Check if roll is three pairs.
        elif len(count) == 3:
            if count[0][1] == 2 and (count[1][1] == 2 or count[1][1] == 4):
                return 'b'
        # Check if there are three or more of a kind.  If three of a kind is for 2s, skip.
        elif count[0][1] >= 3:
            if count[0][0] != 2 or (count[0][0] == 2 and count[0][1] != 3):
                # need to access which dice to return from last_roll
                str_keeper_dice = ''
                for num in range(0, count[0][1] - 1):
                    str_keeper_dice += count[0][0]
                self.report("> ")
#                return '> '
        # Check if there are any 1s and keep a single 1.  If not, check for 5s and keeps a single 5.
        else:
            for num in range(0, len(count)):
                if count[0][num] == 1:
                    self.report("> 1")
#                    return '> 1'
                elif count[0][num] == 5:
                    self.report("> 5")
#                    return '> 1'

        # # if 1 in self.last_roll:
        # #     print('true')
        # roll = GameLogic.get_scorers(self.last_roll)
        # roll_list = list(roll)
        # new_list_ones  = [index for (index, item) in enumerate(self.last_roll) if item == 1]
        # new_list_twos  = [index for (index, item) in enumerate(self.last_roll) if item == 2]
        # new_list_threes  = [index for (index, item) in enumerate(self.last_roll) if item == 3]
        # new_list_fours  = [index for (index, item) in enumerate(self.last_roll) if item == 4]
        # new_list_fives  = [index for (index, item) in enumerate(self.last_roll) if item == 5]
        # print(str(new_list_fives))
        # new_list_sixes  = [index for (index, item) in enumerate(self.last_roll) if item == 6]
        # 
        # 
        # if new_list_ones:
        #     if not self.dice_remaining or self.dice_remaining >= 4:
        #         roll_list.sort()
        #         self.report("> " + (str(roll_list[0])))
        #         roll_list = str(roll_list[0])
        #         return roll_list
        #     else:
        #         roll_list.sort()
        #         if len(roll_list) >= 2:
        #             list_of_ones = ''
        #             for num in roll_list:
        #                 list_of_ones += str(num)
        #             self.report("> " + list_of_ones)
        #             roll_list = str(roll_list)
        #             return roll_list
        # elif new_list_fives:
        #     if not self.dice_remaining or self.dice_remaining >= 4:
        #         if not new_list_ones:
        #             roll_list.sort()
        #             self.report("> " + (str(roll_list[0])))
        #             roll_list = str(roll_list[0])
        #             return roll_list
        #     else:
        #         roll_list.sort()
        #         # if len(roll_list) <= 2:
        #         list_of_fives = ''
        #         for num in roll_list:
        #             list_of_fives += str(num)
        #         self.report("> " + list_of_fives)
        #         roll_list = str(roll_list)
        #         return roll_list
        # return 'r'
        # 
        # # return super()._enter_dice()
