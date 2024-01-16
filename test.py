import g4f

request_for_GPT = 'Напиши калькулятор на Python'

def get_response_GPT(request_for_GPT):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        provider=g4f.Provider.ChatBase,
        messages=[{"role": "user", "content": request_for_GPT}],
        #proxy="http://122.155.165.191:3128",

    )
    return response

#print(f"Result:", get_response_GPT(request_for_GPT))

a = pow(8,2,4)

print(a)