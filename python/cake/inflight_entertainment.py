
def inflight_entertainment(flight_length, movie_lengths):
    '''
    Users on longer flights like to start a second 
    movie right when their first one ends, but they 
    complain that the plane usually lands before they 
    can see the ending. So you're building a feature 
    for choosing two movies whose total runtimes will 
    equal the exact flight length.

    Write a method that takes an integer flightLength 
    (in minutes) and an array of integers 
    movieLengths (in minutes) and returns a boolean 
    indicating whether there are two numbers in 
    movieLengths whose sum equals flightLength.

    When building your method:

    Assume your users will watch exactly two movies
    Don't make your users watch the same movie twice
    Optimize for runtime over memory
    
    https://www.interviewcake.com/question/java/inflight-entertainment?course=fc1&section=hashing-and-hash-tables
    
    Time : O(N)
    Space: O(N)
    Note : 
    '''
    diff_map = {flight_length - mv_ln:None for mv_ln in movie_lengths}
    for oth_ln in movie_lengths:
        if oth_ln in diff_map:
            return True

    return False         


def run():
    movie_lengths = [122, 145, 134, 178, 110, 109, 189]
    flight_length = 300

    print("Can I watch 2 movies? Hell %s" 
          % str(inflight_entertainment(flight_length, movie_lengths)))

if __name__ == '__main__':
    run()

