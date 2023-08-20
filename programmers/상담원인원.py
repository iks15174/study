import math


def solution(k, n, reqs):
    answer = 0
    consultant_cnt_by_counseling_type = [1] * k
    for _ in range(n - k):
        best_conseling_type = get_best_conseling_type_for_add_people(
            reqs, consultant_cnt_by_counseling_type
        )
        consultant_cnt_by_counseling_type[best_conseling_type] += 1

    for counseling_type in range(k):
        reqs_of_counseling_type = list(filter(
            lambda req: req[2] == counseling_type + 1, reqs
        ))
        answer += get_waiting_time(
            reqs_of_counseling_type, consultant_cnt_by_counseling_type[counseling_type]
        )
    return answer


def get_best_conseling_type_for_add_people(reqs, consultant_cnt_by_counseling_type):
    max_reduced_time = -math.inf
    min_reduced_index = -1

    for counseling_type, personnel in enumerate(consultant_cnt_by_counseling_type):
        reqs_of_counseling_type = list(filter(
            lambda req: req[2] == counseling_type + 1, reqs
        ))
        orginal_waiting_time = get_waiting_time(reqs_of_counseling_type, personnel)
        reduced_time = orginal_waiting_time - get_waiting_time(
            reqs_of_counseling_type, personnel + 1
        )
        if reduced_time > max_reduced_time:
            min_reduced_index = counseling_type
            max_reduced_time = reduced_time

    return min_reduced_index


def get_waiting_time(reqs_of_counseling_type, personnel):
    consultation_schedule = init_consultation_schedule(personnel)
    waiting_time = 0
    for start_time, consultation_duration, _ in reqs_of_counseling_type:
        consultant = get_fastest_finish_consultant(consultation_schedule)
        fastest_finish_time = consultation_schedule[consultant]

        if fastest_finish_time <= start_time:
            consultation_schedule[consultant] = start_time + consultation_duration
        else:
            consultation_schedule[consultant] = (
                fastest_finish_time + consultation_duration
            )
            waiting_time += fastest_finish_time - start_time

    return waiting_time


def get_fastest_finish_consultant(consultation_schedule):
    for consultant, finish_time in consultation_schedule.items():
        if min(consultation_schedule.values()) == finish_time:
            return consultant


def init_consultation_schedule(personnel):
    consultation_schedule = {}
    for i in range(personnel):
        consultation_schedule[i] = 0
    return consultation_schedule
