print("Let's practise everything.")
print('You\' need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passiong from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five=10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates


start_point=10000
beans,jars,crates=secret_formula(start_point)

print(f"With a starting point of: {start_point}")
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point=start_point/10
beans,jars,crates=secret_formula(start_point)

print("We can also do that this way:")
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
#print(f"We'd have {secret_formula(start_point)} beans, {secret_formula(start_point)} jars, and {secret_formula(start_point)} crates.")
#print("We'd have %d beans, %d jars, and %d crates."%(secret_formula(start_point)))
