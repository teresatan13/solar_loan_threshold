# Solar loans in 3 states

# Need to apply a threshold for solar applicants based on the Area Median Income (AMI), which is based on household size
# If the applicant's annual household income amount exceeds the AMI for their household size, they are considered ineligible. If it is below the threshold,
# they are considered eligible

# Write a function that takes 3 arguments: state, household size and annual income. Based on the below table of AMI by state, return the client's eligibility status: 
# eligible or ineligible

# Use any language and frameworks that you want. May include a write up that explains any assumptions or design choices that you made


def check_eligibility(state, household_size, annual_income):
    # create 3 dictionaries for each state by household size (index)
    ami_by_state = {
        'Texas': [59710, 68240, 76770, 85300, 92124, 98948, 105772, 112596],
        'Rhode Island': [69510, 79440, 89370, 99300, 107244, 115188, 123132, 131076],
        'Massachusetts': [84280, 96320, 108360, 120400, 130032, 136640, 149296, 158928]
    }
    
    # iterate over the dictionaries to find the correct household size and corresponding ami value
    for i, size in enumerate(range(1, 9)):
        print(i, size)
        
        # if the current size value matches the given household size argument, then we've found the correct household size and can use the corresponding
        # ami value
        if household_size == size:
            # save the ami value for the state household size to a variable
            ami = ami_by_state[state][i]
            # exit the loop once we've found the correct ami value and dont need to continue checking other household sizes
            break

    # ami = ami_by_state[state][household_size - 1]

    # if annual income is below the ami for their household size,
    if annual_income <= ami:
        # they are eligible
        return 'eligible'
    # otherwise if annual income is above,
    else:
        # they are ineligible
        return 'ineligible'



# Tests

def test_1():
    test_name = 'test_texas'
    state = 'Texas'
    household_size = 4
    ami = 85300

    annual_income = 80200

    result = check_eligibility(state, household_size, annual_income)
    expected = 'eligible'

    if result == expected:
        print(f'Passed {test_name}')
    else:
        print(f'FAILED {test_name}!   Expected = {expected}   Output = {result}')


def test_2():
    test_name = 'test_rhode_island'
    state = 'Rhode Island'
    household_size = 1
    ami = 69510

    annual_income = 73500

    result = check_eligibility(state, household_size, annual_income)
    expected = 'ineligible'

    if result == expected:
        print(f'Passed {test_name}')
    else:
        print(f'FAILED {test_name}!   Expected = {expected}   Output = {result}')


def test_3():
    test_name = 'test_massachusetts'
    state = 'Massachusetts'
    household_size = 8
    ami = 158928

    annual_income = 99100

    result = check_eligibility(state, household_size, annual_income)
    expected = 'eligible'

    if result == expected:
        print(f'Passed {test_name}')
    else:
        print(f'FAILED {test_name}!   Expected = {expected}   Output = {result}')


def test_4():
    test_name = 'test_texas'
    state = 'Texas'
    household_size = 3
    ami = 76770

    annual_income = 40024

    result = check_eligibility(state, household_size, annual_income)
    expected = 'eligible'

    if result == expected:
        print(f'Passed {test_name}')
    else:
        print(f'FAILED {test_name}!   Expected = {expected}   Output = {result}')


def test_5():
    test_name = 'test_texas'
    state = 'Texas'
    household_size = 1
    ami = 59710

    annual_income = 40024

    result = check_eligibility(state, household_size, annual_income)
    expected = 'eligible'

    if result == expected:
        print(f'Passed {test_name}')
    else:
        print(f'FAILED {test_name}!   Expected = {expected}   Output = {result}')



test_1()
test_2()
test_3()
test_4()
test_5()