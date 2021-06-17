test_dict = [{
    'name': 'John',
    'age': 16
},
    {
        'name': 'Amy',
        'age': 20
    }
]

print(test_dict)

test_dict.remove({
    'name': 'John'
})

print(test_dict)