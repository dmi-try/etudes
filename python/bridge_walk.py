#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задачка: четверо друзей переходят через мост с одним фонариком.
# Одновременно по мосту могут идти только двое. Один из друзей
# переходит мост за минуту, второй за 2, третий за 5 и четвёртый
# за 10. Найти наименьшее время, за которое все окажутся на другой
# стороне.

# Идея решать задачу построением дерева состояний конечного автомата
# и нахождением кратчайшего маршрута. Интересно не закладываться на
# то, что каждый раз в одну сторону идут двое, а возвращается с фонариком
# один. Такое допущение может лишить задачу интересных решений.

# У задачи в такой формулировке есть решение в 17 минут. Хочется решить
# общий случай для N друзей, переходящих мост за T[i] минут и прочности
# моста в K человек.

# Тривиальное решение: первый переводит всех остальных по очереди. Оно
# может служить ограничением на определение длительности других решений.
# Можно было бы оптимизировать тривиальное решение, чтоб переводил
# самый быстрый, начиная с самых медленных. Что позволит сгруппировать
# переводимых по близости скоростей. Но можно обойтись и без оптимизации.
# Проще всего запрограммировать, чтоб переводил самый быстрый всех по одному.

# В данной версии программы вперёд идёт максимум людей, а возвращается
# только один. Для более общего случая надо предусмотреть возможность
# циклов на графе. Что как бы намекает о неоптимальности подобных стратегий.

from itertools import combinations
from copy import deepcopy

friends_speeds = [1, 2, 5, 10]
bridge_capacity = 2

def trivial_solution(speeds):
    fastest_speed = min(speeds)
    forward_time = sum(speeds) - fastest_speed
    backward_time = fastest_speed * (len(speeds) - 2)
    return forward_time + backward_time

# Для заданных условий тривиальным решением является 19 минут:
# 1 и 2 направо, 1 налево, 1 и 5 направо, 1 налево, 1 и 10 направо
# 2 + 1 + 5 + 1 + 10 = 19
assert trivial_solution([1, 2, 5, 10]) == 19

initial_state = {
    'before_bridge': friends_speeds,
    'after_bridge': [],
    'time_elapsed': 0,
    'time_limit': trivial_solution(friends_speeds),
    'bridge_capacity': bridge_capacity,
    'previous_state': None,
    'description': '',
    'next_states': [],
    'debug': ''
}

final_states = []

def gen_state(prev_state, go_forward, go_backward=None):
    new_state = deepcopy(prev_state)
    for i in go_forward:
        new_state['before_bridge'].remove(i)
        new_state['after_bridge'].append(i)
    if go_backward:
        for i in go_backward:
            new_state['after_bridge'].remove(i)
            new_state['before_bridge'].append(i)
    new_state['time_elapsed'] += max(go_forward)
    new_state['description'] = "%s go forward" % list(go_forward)
    new_state['next_states'] = calc_next_states(new_state)
    if go_backward:
        new_state['description'] += ", %s go backward" % list(go_backward)
        new_state['time_elapsed'] += max(go_backward)
    new_state['previous_state'] = prev_state
    return new_state

def print_solution(state):
    print "Found solution: %d minutes" % state['time_elapsed']
    description = state['description']
    i = state['previous_state']
    while i['description']:
        description = i['description'] + '\n' + description
        i = i['previous_state']
    print "Steps:\n", description

def calc_next_states(state):
    if state['time_elapsed'] >= state['time_limit']:
        return []
    if state['before_bridge'] == []:
        return []
    if len(state['before_bridge']) <= state['bridge_capacity']:
        new_final_state = gen_state(state, state['before_bridge'])
        final_states.append(new_final_state)
        return [new_final_state]
    result = []
    for l in [state['bridge_capacity']]:
        for go_forward in combinations(state['before_bridge'], l):
            for l in [1]:
                for go_backward in combinations(state['after_bridge'] + list(go_forward), l):
                    if go_forward != go_backward:
                        result.append(gen_state(state, go_forward, go_backward))
    return result

min_time = initial_state['time_limit']
calc_next_states(initial_state)

for i in final_states:
    if i['time_elapsed'] < min_time:
        min_time = i['time_elapsed']

for i in final_states:
    if i['time_elapsed'] == min_time:
        print_solution(i)
