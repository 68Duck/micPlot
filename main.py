
def table_print(table,col_first = True):
    if col_first:
        max_len = max([len(row) for row in table])
        for i in range(max_len):
            str = ""
            for j in range(len(table)):
                if len(table[j]) > i:
                    if table[j][i] is None:
                        str = str + "/" + " "
                    else:
                        str = str + table[j][i] + " "
            print(str)


    else:
        for row in table:
            print(row)

def calculate_score(plot):
    changes = 0
    max_len = max([len(row) for row in plot])
    for i in range(max_len):
        for j in range(len(plot)):
            if len(plot[j]) > i:
                if j == 0:
                    prev = plot[j][i]
                else:
                    if plot[j][i] is None:
                        pass
                    elif prev is None:
                        prev = plot[j][i]
                    else:
                        if prev != plot[j][i]:
                            changes += 1
                            prev = plot[j][i]

    return changes

def calculate_score2(plot):
    changes = 0
    change_distance = 0
    # max_len = max([len(row) for row in plot])
    # for i in range(max_len):
    #     for j in range(len(plot)):
    #         if plot[j][i] is None:
    #             updated = False
    #             for k in range(j,len(plot),1):
    #                 # print(j,i,k,max_len)
    #                 print(plot[k][i])
    #                 if plot[k][i] is not None:
    #                     for l in range(j,j+k-1,1):
    #                         plot[l][i] = plot[k][i]
    #                     updated = True
    #                     break
    #             if not updated:
    #                 if j>0:
    #                     plot[j][i] = plot[j-1][i]
    # table_print(plot)
    before_none = None
    max_len = max([len(row) for row in plot])
    for i in range(max_len):
        none_counter = 0
        for j in range(len(plot)):
            if len(plot[j]) > i:
                if j == 0:
                    prev = plot[j][i]
                else:
                    if plot[j][i] is None:
                        if j < len(plot)-1:
                            if before_none is not None:
                                if plot[j+1][i] == before_none:
                                    none_counter = -1

                        none_counter += 1
                        if prev is not None:
                            before_none = prev
                    elif prev is None:
                        # if plot[j][i] is not None:
                        #     if before_none == plot[j][i]:
                        prev = plot[j][i]
                        none_counter = 0
                    else:
                        # print(none_counter,j,i)
                        if prev != plot[j][i]:
                            changes += 1
                            # if none_counter:
                            #     print(before_none,prev)
                            #     if prev != before_none:
                            change_distance += none_counter
                            prev = plot[j][i]
                            none_counter = 0


    score = 1000*changes - change_distance
    return score


def solve(mics,plot,scenes,current_scene_number):
    for i in range(current_scene_number,len(scenes),1):
        col = scenes[i]
        if len(plot) > current_scene_number:
            column = plot[current_scene_number]
            plot.remove(column)
            # input(column)
        else:
            column = [None]*mics
        if i == 0:
            for v,val in enumerate(col):
                column[v] = val
        else:
            prev = plot[i-1]
            for v, val in enumerate(col):
                if val in prev:
                    index = prev.index(val)
                    column[index] = val

            for v,val in enumerate(col):
                if val not in column:
                    indexes = []
                    for w,item in enumerate(column):
                        if item is None:
                            indexes.append(w)
                    plots = []
                    min = 10000000
                    min_plot = None
                    for i in indexes:
                        new_column = column[:]
                        new_column[i] = val
                        new_plot = plot[:]
                        new_plot.append(new_column)
                        new_plot = solve(mics,new_plot,scenes,current_scene_number)
                        score = calculate_score2(new_plot)
                        # print(new_plot)
                        # print(score)
                        if score < min:
                            min = score
                            min_plot = new_plot
                    return min_plot



        current_scene_number += 1
        plot.append(column)
    # input(plot)
    return plot


def solve2(mics,plot,scenes,current_scene_number):
    for i in range(current_scene_number,len(scenes),1):
        col = scenes[i]
        if len(plot) > current_scene_number:
            column = plot[current_scene_number]
            plot.remove(column)
            # input(column)
        else:
            column = [None]*mics
        if i == 0:
            for v,val in enumerate(col):
                column[v] = val
        else:
            prev = plot[i-1][:]
            # print(prev)
            for p,prev_item in enumerate(prev):
                if prev_item is None:
                    for j in range(i-1):
                        if plot[i-j-2][p] is not None:
                            prev[p] = plot[i-j-2][p]
                            break
            # print(prev)
            # print(col)
            for v, val in enumerate(col):
                if val in prev:
                    index = prev.index(val)
                    column[index] = val

            for v,val in enumerate(col):
                if val not in column:
                    indexes = []
                    for w,item in enumerate(column):
                        if item is None:
                            indexes.append(w)
                    plots = []
                    min = 10000000
                    min_plot = None
                    for i in indexes:
                        new_column = column[:]
                        new_column[i] = val
                        new_plot = plot[:]
                        new_plot.append(new_column)
                        new_plot = solve2(mics,new_plot,scenes,current_scene_number)
                        score = calculate_score2(new_plot)
                        print(new_plot)
                        # print(score)
                        if score < min:
                            min = score
                            min_plot = new_plot
                    return min_plot
            # print("test")



        current_scene_number += 1
        plot.append(column)
    # input(plot)
    return plot

def solve4(mics,plot,scenes,current_scene_number):
    for i in range(current_scene_number,len(scenes),1):
        col = scenes[i]
        if len(plot) > current_scene_number:
            column = plot[current_scene_number]
            plot.remove(column)
            # input(column)
        else:
            column = [None]*mics
        if i == 0:
            for v,val in enumerate(col):
                column[v] = val
        else:
            prev = plot[i-1][:]
            # print(prev)
            for p,prev_item in enumerate(prev):
                if prev_item is None:
                    for j in range(i-1):
                        if plot[i-j-2][p] is not None:
                            prev[p] = plot[i-j-2][p]
                            break
            # print(prev)
            # print(col)
            for v, val in enumerate(col):
                if val in prev:
                    index = prev.index(val)
                    column[index] = val

            changeable_inputted = [val for val in column if val not in prev and val is not None]
            # print(column)
            # print(changeable_inputted)


            for v,val in enumerate(col):
                if val not in column:
                    indexes = []
                    for w,item in enumerate(column):
                        if item is None:
                            indexes.append(w)
                    plots = []
                    min = 10000000
                    min_plot = None
                    # print(indexes,val)
                    max_changeable_index = 0
                    for changeable in changeable_inputted:
                        if sorted([changeable,val]) == [changeable,val]:
                            changeable_index = column.index(changeable)
                            max_changeable_index = max(max_changeable_index,changeable_index)


                    for i in indexes:
                        if i>max_changeable_index:
                            new_column = column[:]
                            new_column[i] = val
                            new_plot = plot[:]
                            new_plot.append(new_column)
                            new_plot = solve4(mics,new_plot,scenes,current_scene_number)
                            # print(new_plot)
                            if new_plot is None:
                                continue
                            score = calculate_score2(new_plot)
                            # print(score)
                            if score < min:
                                min = score
                                min_plot = new_plot
                        # else:
                        #     print(i)
                    return min_plot
            # print("test")



        current_scene_number += 1
        plot.append(column)
    # input(plot)
    return plot


def solve5(mics,plot,scenes,current_scene_number):
    for i in range(current_scene_number,len(scenes),1):
        col = scenes[i]
        if len(plot) > current_scene_number:
            column = plot[current_scene_number]
            plot.remove(column)
            # input(column)
        else:
            column = [None]*mics
        if i == 0:
            for v,val in enumerate(col):
                column[v] = val
        else:
            prev = plot[i-1][:]
            # print(prev)
            for p,prev_item in enumerate(prev):
                if prev_item is None:
                    for j in range(i-1):
                        if plot[i-j-2][p] is not None:
                            prev[p] = plot[i-j-2][p]
                            break
            # print(prev)
            # print(col)
            for v, val in enumerate(col):
                if val in prev:
                    index = prev.index(val)
                    column[index] = val

            changeable_inputted = [val for val in column if val not in prev and val is not None]
            # print(column)
            # print(changeable_inputted)



            for v,val in enumerate(col):
                if val not in column:
                    max_changeable_index = 0
                    for changeable in changeable_inputted:
                        if sorted([changeable,val]) == [changeable,val]:
                            changeable_index = column.index(changeable)
                            max_changeable_index = max(max_changeable_index,changeable_index)
                    indexes = []
                    for w,item in enumerate(column):
                        if item is None:
                            if w >= max_changeable_index:
                                indexes.append(w)
                    plots = []
                    min = 10000000
                    min_plot = None
                    # print(indexes,val)


                    for i in indexes:
                        new_column = column[:]
                        new_column[i] = val
                        new_plot = plot[:]
                        new_plot.append(new_column)
                        # print(new_plot)
                        new_plot = solve5(mics,new_plot,scenes,current_scene_number)
                        if new_plot is None:
                            continue
                        # else:
                            # print(new_plot)
                        score = calculate_score2(new_plot)
                        # print(score)
                        if score < min:
                            min = score
                            min_plot = new_plot
                        # else:
                        #     print(i)
                    return min_plot
            # print("test")



        current_scene_number += 1
        plot.append(column)
    # input(plot)
    return plot


def solve3(mics,plot,scenes,current_scene_number):
    for i in range(current_scene_number,len(scenes),1):
        col = scenes[i]
        if len(plot) > current_scene_number:
            column = plot[current_scene_number]
            plot.remove(column)
            # input(column)
        else:
            column = [None]*mics
        if i == 0:
            for v,val in enumerate(col):
                column[v] = val
        else:
            prev = plot[i-1][:]
            # print(prev)
            for p,prev_item in enumerate(prev):
                if prev_item is None:
                    for j in range(i-1):
                        if plot[i-j-2][p] is not None:
                            prev[p] = plot[i-j-2][p]
                            break
            # print(prev)
            # print(col)
            for v, val in enumerate(col):
                if val in prev:
                    index = prev.index(val)
                    column[index] = val

            changeable_inputted = [val for val in column if val not in prev and val is not None]


            for v,val in enumerate(col):
                if val not in column:
                    indexes = []
                    for w,item in enumerate(column):
                        if item is None:
                            indexes.append(w)
                    plots = []
                    min = 10000000
                    min_plot = None
                    for i in indexes:
                        for changeable in changeable_inputted:
                            if sorted([changeable,val]) == [changeable,val]:
                                changeable_index = column.index(changeable)
                                if changeable_index > i:
                                    indexes.remove(i)
                                    break



                    for i in indexes:
                        new_column = column[:]
                        new_column[i] = val
                        new_plot = plot[:]
                        new_plot.append(new_column)
                        new_plot = solve3(mics,new_plot,scenes,current_scene_number)
                        score = calculate_score2(new_plot)
                        # print(new_plot)
                        # print(score)
                        if score < min:
                            min = score
                            min_plot = new_plot
                    return min_plot
            # print("test")



        current_scene_number += 1
        plot.append(column)
    # input(plot)
    return plot

def main_2(scenes,mics):
    # scenes = [["A","B","C","D","E"],["C","F","G"],["C","F"],["A","B","C","D"],["C","H","I"]]
    # scenes = [scene.sort() for scene in scenes]
    scenes = [sorted(scene) for scene in scenes]
    plot = []
    current_scene_number = 0 #zero indexed
    plot = solve5(mics,plot,scenes,current_scene_number)
    print(plot)
    table_print(plot)
    print(calculate_score2(plot))

def main():
    mics = 4
    arr = [["A","B","C","D","E"],["C","F","G"],["C","F"],["A","B","C","D"],["C","H","I"]] #scenes
    plot = []
    for i,col in enumerate(arr):
        column = [None]*mics
        if i == 0:
            for v,val in enumerate(col):
                column[v] = val
        else:
            prev = plot[i-1]
            for v, val in enumerate(col):
                if val in prev:
                    index = prev.index(val)
                    column[index] = val

            for v,val in enumerate(col):
                if val not in column:
                    for w,item in enumerate(column):
                        if item == None:
                            column[w] = val
                            break



        plot.append(column)

    print(plot)

    table_print(plot)




if __name__ == "__main__":
    # arr = [['A', 'B', 'C', 'D', 'E'], ['F', None, 'C', None, 'G'], ['F', None, 'C', None, None], ['A', 'Z', 'C', 'D', None], ['H', None, 'C', None, "I"]]
    arr = [['A', 'B', 'C', 'D', 'E'], ['F', None, 'C', None, 'G'], ['F', None, 'C', None, None], ['A', 'B', 'C', 'D', None], ['H', 'I', 'C', None, None]]
    # table_print(arr)
    # print(calculate_score2(arr))
    mics = 7
    arr = [['Heath', 'Dewey', 'Theo', 'Ashwin', 'Harry'], ['Ned', 'Patty', 'Dewey'], ['Dewey', 'Ned'], ['Dewey', 'Heath', 'Theo', 'Louis'], ['Sophie', 'Shonelle', 'Dewey'], ['Dewey', 'Felix'], ['Dewey'], ['Dewey', 'Rosalie'], ['Rosalie', 'Heath', 'Zack', 'Summer', 'Hannah', 'Will Tackley', 'Noah', 'Louis', 'Amelia'], ['Rosalie'], ['Dewey', 'Rosalie', 'Ms Sheinkopf'], ['Dewey', 'Rosalie', 'Lucy', 'Louis'], ['Dewey', 'Rosalie', 'Ms Sheinkopf', 'Summer', 'Lawrence', 'Freddy', 'Zack'], ['Dewey', 'Ned', 'Patty'], ['Dewey', 'Gabe'], ['Rosalie'], ['Rosalie', 'Summer'], ['Dewey', 'Summer', 'Lawrence', 'Marcy', 'Zack', 'Katie', 'Freddy', 'James', 'Shonelle', 'Billy', 'Madison', 'Mason', 'Sophie', 'Tomika'], ['Felix', 'Freddy', 'Rajun', 'Billy', 'Tomika', 'Will Tackley', 'Noah', 'Heath', 'Zack'], ['Zack', 'Billy', 'Freddy', 'Lawrence', 'Madison', 'Shonelle', 'Mason'], ['Dewey', 'Marcy', 'Mason', 'Billy', 'Summer', 'Lawrence', 'Shonelle', 'Freddy', 'Zack'], ['Gabe', 'Hannah', 'Lucy', 'Ms Sheinkopf', 'Will Tackley', 'Leah', 'Noah', 'Rosie', 'Felix', 'Dewey', 'Rosalie', 'Louis'], ['Dewey', 'Rosalie', 'Gabe', 'Ms Sheinkopf'], ['Dewey', 'Shonelle', 'Marcy', 'Freddy', 'Zack', 'Mason', 'Summer', 'Billy', 'Lawrence', 'Katie', 'James', 'Rosalie', 'Sophie', 'Madison'], ['Dewey', 'Zack'], ['Mason', 'Dewey', 'Summer', 'Zack', 'Marcy', 'Lawrence', 'Rajun', 'Shonelle', 'Tomika']]
    # arr = [['Dewey', 'Shonelle', 'Marcy', 'Freddy', 'Zack', 'Mason', 'Summer', 'Billy', 'Lawrence', 'Katie', 'James', 'Rosalie', 'Sophie', 'Madison'], ['Dewey', 'Zack'], ['Mason', 'Dewey', 'Summer', 'Zack', 'Marcy', 'Lawrence', 'Rajun', 'Shonelle', 'Tomika']]
    arr = [['Heath', 'Dewey', 'Theo', 'Ashwin', 'Harry'], ['Ned', 'Patty', 'Dewey'], ['Dewey', 'Ned'], ['Dewey', 'Heath', 'Theo', 'Louis'], ['Sophie', 'Shonelle', 'Dewey'], ['Dewey', 'Felix'], ['Dewey'], ['Dewey', 'Rosalie'],['Rosalie', 'Heath', 'Zack', 'Summer', 'Hannah', 'Will Tackley', 'Noah', 'Louis', 'Amelia']]
    # arr = [['Heath', 'Dewey', 'Theo', 'Ashwin', 'Harry'], ['Ned', 'Patty', 'Dewey'], ['Dewey', 'Ned'], ['Dewey', 'Heath', 'Theo', 'Louis'], ['Sophie', 'Shonelle', 'Dewey'], ['Dewey', 'Felix'], ['Dewey'], ['Dewey', 'Rosalie']]

    # arr = [['Dewey', 'Summer', 'Lawrence', 'Marcy', 'Zack', 'Katie', 'Freddy', 'James', 'Shonelle', 'Billy', 'Madison', 'Mason', 'Sophie', 'Tomika'], ['Felix', 'Freddy', 'Rajun', 'Billy', 'Tomika', 'Will Tackley', 'Noah', 'Heath', 'Zack'], ['Zack', 'Billy', 'Freddy', 'Lawrence', 'Madison', 'Shonelle', 'Mason'], ['Dewey', 'Marcy', 'Mason', 'Billy', 'Summer', 'Lawrence', 'Shonelle', 'Freddy', 'Zack'], ['Gabe', 'Hannah', 'Lucy', 'Ms Sheinkopf', 'Will Tackley', 'Leah', 'Noah', 'Rosie', 'Felix', 'Dewey', 'Rosalie', 'Louis']]
    main_2(arr,mics)
