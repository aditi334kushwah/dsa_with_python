class Solution(object):
    def numRescueBoats(self, people, limit):

        people.sort()
        
        boatcount = 0

        left = 0 
        right = len(people) -1

        while left <= right :

            sum = people[left] + people[right]

            if sum <=  limit :

                boatcount += 1
                left += 1
                right -= 1

            else :

                boatcount += 1
             
                right -= 1

            

        return boatcount