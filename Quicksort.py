class Quicksort(object):

    def __init__(self):
        self.DEBUG = True

    def debug(self, message):
        if self.DEBUG:
            print(message)

    def swap(self, list_for_swap, a, b):
        self.debug("list_for_swap: " + str(list_for_swap))
        self.debug("a = " + str(a)  + ", b = "  + str(b))
        self.debug("Swapping " + str(list_for_swap[a]) + " for " + str(list_for_swap[b]))
        temp = list_for_swap[a]
        list_for_swap[a] = list_for_swap[b]
        list_for_swap[b] = temp
        return list_for_swap

    def sort(self, somelist):


        list_to_return = somelist

        self.debug("Beginning to sort list: " + str(somelist))

        PIVOT = self.get_pivot_subscript(somelist)
        wall_0 = self.get_wall_subscript_initial(somelist)
        peek_0 = self.get_peek_subscript_initial(somelist)

        for wall_i in range(wall_0, PIVOT):
            for peek_i in range(wall_i, PIVOT - 1):

                self.debug(str(somelist[peek_i]) + " <  " + str(somelist[PIVOT]))
                if somelist[peek_i] < somelist[PIVOT]:
                    self.debug("True")
                    if peek_i != wall_i:
                        list_to_return = self.swap(list_to_return, peek_i, wall_i)
                    else:
                        self.debug("Skipping swap: wall_i == peek_i")
                    wall_i += 1
                else:
                    self.debug("False")

                self.debug("")

            list_to_return = self.swap(list_to_return, wall_i, PIVOT)

        return somelist

    def get_pivot_subscript(self, somelist):
        return len(somelist) - 1

    def get_wall_subscript_initial(self, somelist):
        return 0

    def get_peek_subscript_initial(self, somelist):
        return 0
