# Name: Harsh Gupta
# Student #: 300042828
# ITI 1120 C - Assignment 4

import random

def binary_search(L, v) -> int:
    """ (list, object) -> int
         Return the index of the first occurrence of value in L, or return
         -1 if value is not in L.
    """
    # Mark the beginning and the end indices of the unexplored sublist.
    b = 0
    e = len(L) - 1

    while b != e + 1:
        mid = (b + e) // 2
        if L[mid] < v:
            b = mid + 1
        else:
            e = mid - 1

    if 0 <= b < len(L) and L[b] == v:
        return b
    else:
        return -1

def create_network(file_name):
    """(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social network. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the friendship network as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friends is sorted).
    """

    friends = open(file_name).read().splitlines()

    # YOUR CODE GOES HERE

    numUsers = int(friends[0])
    friendships = friends[1:]
    listsOfFriends = []
    for i in range(len(friendships)):
        twoFriends = friendships[i].split(sep=" ")
        twoFriends[0] = int(twoFriends[0])
        twoFriends[1] = int(twoFriends[1])
        listsOfFriends.append(twoFriends)

    network = []
    currentFriend = listsOfFriends[0][0]
    network.append((currentFriend, [listsOfFriends[0][1]]))
    network.append((listsOfFriends[0][1], [listsOfFriends[0][0]]))
    whereIsCurrent = 0
    for i in range(1, len(listsOfFriends)):
        network.sort()
        if listsOfFriends[i][0] == currentFriend:
            network[whereIsCurrent][1].append(listsOfFriends[i][1])
            #network.sort()
            pos = binary_search([j[0] for j in network], listsOfFriends[i][1])
            if pos == -1:
                network.append((listsOfFriends[i][1], [currentFriend]))
            else:
                network[pos][1].append(currentFriend)

        else:
            currentFriend = listsOfFriends[i][0]
            whereIsCurrent = binary_search([j[0] for j in network], currentFriend)

            #network.sort()
            pos = whereIsCurrent
            #binary_search([j[0] for j in network], currentFriend)
            if pos == -1:
                network.append((currentFriend, [listsOfFriends[i][1]]))
            else:
                network[pos][1].append(listsOfFriends[i][1])

            #network.append((currentFriend, [listsOfFriends[i][1]]))

            #network.sort()
            pos = binary_search([j[0] for j in network], listsOfFriends[i][1])
            if pos == -1:
                network.append((listsOfFriends[i][1], [currentFriend]))
            else:
                network[pos][1].append(currentFriend)

    #network.sort()
    #for i in network:
        #i[1].sort()

    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''

    common=[]
    friendsOf1 = []
    friendsOf2 = []
    # YOUR CODE GOES HERE

    usersInNet = [i[0]for i in network] #O(n)

    friendsOf1 = network[binary_search(usersInNet, user1)][1] #O(log(n))
    friendsOf2 = network[binary_search(usersInNet, user2)][1] #O(log(n))

    # O(n+ log(n))

    """
    for i in network:
        if i[0] == user1:
            friendsOf1 = i[1]
        if i[0] == user2:
            friendsOf2 = i[1]
        if len(friendsOf1) and len(friendsOf2):
            break
    """

    for i in friendsOf1:
        if binary_search(friendsOf2, i) != -1:
            common.append(i)

    # O(n + log(n) + n1*log(n2))
    # O(log(n) + n1 + n2)
    # common.sort()

    return common

#print(getCommonFriends(3,1,create_network("net1.txt")))
    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    counter = 0
    max = 0
    newBFF = None
    for i in network:
        if i[0] == user:
            allMyFriends = i[1]
            break

    for i in network:
        counter = 0
        if i[0] != user and (i[0] not in allMyFriends):
            counter = len(getCommonFriends(user, i[0], network))

            if counter > max:
                max = counter
                newBFF = i[0]

    return newBFF
    # pass

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    counter = 0
    for i in network:
        if len(i[1]) >= k:
            counter += 1

    return counter
    # pass

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    maxFriends = 0
    for i in network:
        if len(i[1]) > maxFriends:
            maxFriends = len(i[1])

    return maxFriends

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
    maxNum = maximum_num_friends(network)
    for i in network:
        if len(i[1]) == maxNum:
            max_friends.append(i[0])

    return max_friends

def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    return sum(len(i[1]) for i in network) / len(network)
    # pass

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE

    maxFriends = maximum_num_friends(network)
    lNet = len(network)

    return maxFriends == (lNet - 1)

    #for i in network:
        #if len(i[1]) == (len(network) - 1):
            #return True

    #return False

####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    users = [i[0] for i in network]
    user_id = input("Enter an integer for a user ID:")
    isUIDinNet = False
    while not isUIDinNet:
        try:
            user_id = int(user_id)
        except ValueError:
            print("That was not an integer. Please try again.")
            user_id = input("Enter an integer for a user ID:")
        else:
            if user_id not in users:
                print("That user ID does not exist. Try again.")
                user_id = input("Enter an integer for a user ID:")
            else:
                return user_id

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommed the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinaly, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
