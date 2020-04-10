def bubble_sort(random_list):
    ''' take each value adjacent with each other and swap
    values when right side value is less than left side.
    This will push the greater value to the end of the list
    and eventually, with each pass through the list, become
    sorted.'''
    
    #loop tracking the next position we are loading, starting with
    #last position of the list and moving forward
    for next_largest_location in range(len(random_list) - 1, 0, -1):
    
        #loop list and swap adjacent values until reach the position
        #we are loading.  This value will be the "next largest" in the list
        for i in range(next_largest_location):
            if random_list[i] > random_list[i+1]:
                random_list[i],random_list[i+1] = random_list[i+1],random_list[i]

    #sorted list
    return random_list

def selection_sort(random_list):
    ''' pass through the full list determining largest value.  Once full list
    evaluated, load this value into next location being populated which will
    start from the end and work forward, swapping its current value into the
    slot that held the largest.'''
    
    #loop tracking the next position we are loading, starting with
    #last position of the list and moving forward
    for next_largest_location in range(len(random_list) - 1, 0, -1):
        
        #tracks where largest value is stored
        index_with_largest_value = 0
        
        #loop looking for largest value in list
        for i in range(next_largest_location+1):
            
            #if value is larger than that being tracked as "largest",
            #update to track new location.
            if random_list[index_with_largest_value] < random_list[i]:
                index_with_largest_value = i
        
        #swap values placing largest value in its location
        random_list[index_with_largest_value],random_list[next_largest_location] = random_list[next_largest_location],random_list[index_with_largest_value]
    
    return random_list

def insertion_sort(random_list):
    '''read through list to determine "next" value in list's proper location based on
    list's prior values. While reading through these prior values, the values are swapping
    positions to the right to make room for new value.'''

    #loop list once from 2nd element through the length of list
    for i in range(1,len(random_list)):
        
        #tracks preceding location in list for comparing value
        location_prior = i
        current_value = random_list[i]
        
        #find where current value fits logically in those values preceding
        while current_value < random_list[location_prior-1] and location_prior > 0:
            random_list[location_prior] = random_list[location_prior-1]
            location_prior = location_prior - 1
        
        #found proper location so add the current value into list
        random_list[location_prior] = current_value
     
    return random_list
        


print(bubble_sort([5,6,8,9,1,2,4,3,10,7,0]))
print(selection_sort([5,6,8,9,1,2,4,3,10,7,0]))
print(insertion_sort([5,6,8,9,1,2,4,3,10,7,0]))