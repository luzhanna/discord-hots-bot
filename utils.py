import random


def take_random_build(hero):

	talents = hero['talents']
	build = []

	for i in range(7):
		num = random.randint(1,talents[i])
		build.append(num)

	if hero['ult'] == 'c':
		while build[3] + build[6] == 3:
			build[6] = random.randint(1,talents[6])
	else:
		if hero['name'] == 'varian':
			while build[6] not in [build[1], 4, 5]:
				build[6] = random.randint(1,talents[6])

	return build


def take_random_hero(lst):
	num = random.randint(0, len(lst)-1)
	return lst[num]


def take_hero(hero_name, lst):

	name = hero_name.strip().lower()
	name = ''.join([i for i in name if i.isalpha()])

	for hero in lst:
		
		if hero['name'].startswith(name[:5]):
			return hero
		elif name.startswith(hero['alts']):
			return hero

	return ValueError


def take_heroes_of_role(string, lst):

	roles = string.strip().lower().split(',')
	new_list = []

	for hero in lst:
		if hero['role'] in roles:
			new_list.append(hero)

	return new_list


def finalize_output(build, hero):
	output = '[' + 'T' + ''.join(map(str,build)) + ',' + hero['name'] + ']'
	return output


'''MAIN FUNCTIONS'''

def random_hero(lst):

	hero = take_random_hero(lst)
	build = take_random_build(hero)

	return finalize_output(build, hero)


def roled_hero(roles, lst):

	heroes = take_heroes_of_role(roles, lst)
	hero = take_random_hero(heroes)
	build = take_random_build(hero)

	return finalize_output(build, hero)


def hero_build(hero_name, lst):

	hero = take_hero(hero_name, lst)
	build = take_random_build(hero)

	return finalize_output(build, hero)
