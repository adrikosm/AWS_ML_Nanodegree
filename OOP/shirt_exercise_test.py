def run_tests(shirt_one, shirt_two, total_cost, total_discount):

    # Unit tests to check your solution
    assert shirt_one.price == 25, 'shirt_one price should be 25'
    assert shirt_one.color == 'red', ' shirt_one should be red'
    assert shirt_one.style == 'long-sleeve', 'shirt_one should be long_sleeve style'
    assert shirt_one.size == 'S', 'shirt_one size should be S'

    assert shirt_two.price == 10, 'shirt_two price should be 10'
    assert shirt_two.color == 'orange', 'shirt_two should be orange'
    assert shirt_two.style == 'short-sleeve', 'shirt_two should be short_sleeve style'
    assert shirt_two.size == 'L', 'shirt_two size should be L'

    assert total_cost == 35, 'the total_cost of both shirts should be 35'

    assert int(round(total_discount)) == 30, 'total_discount should be 30'
