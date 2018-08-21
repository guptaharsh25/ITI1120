import time
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

    start_time = time.clock()
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


    print(time.clock() - start_time, "seconds")
    return network

print(create_network2("net1.txt"))

"""
def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    start_time = time.clock()
    friends = open(file_name).read().splitlines()

    # YOUR CODE GOES HERE

    numUsers = int(friends[0])
    friendships = friends[1:]
    listsOfFriends = []
    for i in range(len(friendships)):
        twoFriends = friendships[i].split(sep = " ")
        twoFriends[0] = int(twoFriends[0])
        twoFriends[1] = int(twoFriends[1])
        listsOfFriends.append(twoFriends)

    network = []

    count = 0
    userID = 0
    while count < numUsers:
        friendsOfThisUser = []
        for i in listsOfFriends:
            if userID in i:
                if i[0] == userID:
                    friendsOfThisUser.append(i[1])
                else:
                    friendsOfThisUser.append(i[0])
        if len(friendsOfThisUser) > 0:
            friendsOfThisUser.sort()
            oneFriendInNetwork = (userID, friendsOfThisUser)
            network.append(oneFriendInNetwork)
            count += 1
        userID += 1

    return network


def create_network2(file_name):
    (str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

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

    start_time = time.clock()
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
    friendsOfThisUser = []
    for i in listsOfFriends:
        users = [j[0] for j in network]
        if i[0] not in users and len(network):
            #print(i[0], friendsOfThisUser, network)
            network[len(network) - 1].append(friendsOfThisUser)
            friendsOfThisUser = []
            network.append([i[0]])
        elif i[0] not in users:
            friendsOfThisUser = []
            network.append([i[0]])
        friendsOfThisUser.append(i[1])
        if listsOfFriends.index(i) == (len(listsOfFriends) - 1):
            network[len(network) - 1].append(friendsOfThisUser)

    for i in range(len(network)):
        id = network[i][0]
        try:
            id_friends = network[i][1]
        except:
            id_friends = []
        network[i] = (id, id_friends)


    for i in listsOfFriends:
        users = [j[0] for j in network]

        if i[1] not in users:
            users.append(i[1])
            network.append((i[1], []))

        if not network[users.index(i[1])][1].count(i[0]):
            network[users.index(i[1])][1].append(i[0])

        if i[0] not in [j[0] for j in network] and len(network):
            network[len(network) - 1].append(friendsOfThisUser)
            friendsOfThisUser = []
            network.append([i[0]])
        elif i[0] not in [j[0] for j in network]:
            friendsOfThisUser = []
            network.append([i[0]])
        friendsOfThisUser.append(i[1])

    network.sort()
    for i in range(len(network)):
        id = network[i][0]
        try:
            id_friends = network[i][1]
            id_friends.sort()
        except:
            id_friends = []
        network[i] = (id, id_friends)

    print(time.clock() - start_time, "seconds")
    return network

#print(create_network2("huge.txt")[200:202])

"""
