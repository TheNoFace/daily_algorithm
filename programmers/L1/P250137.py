# https://school.programmers.co.kr/learn/courses/30/lessons/250137
# [PCCP 기출문제] 1번 / 붕대 감기


def solution(bandage, health, attacks):
    answer = health
    last_time = 0

    for attack in attacks:
        # 공격 시간만큼 시간을 흘려서 체력 및 연속 회복 시간 계산?
        attack_time = attack[0]
        cumm_heal = 0

        # 직전 공격 시간과 이번 공격 시간의 차이만큼 회복 계산
        for i in range(attack_time - last_time):
            cumm_heal += 1

            # 공격 먼저 하고 보너스 회복 계산
            if i + 1 == (attack_time - last_time):
                answer -= attack[1]
                if answer <= 0:
                    return -1
            else:
                # 연속 시전시간 계산
                if cumm_heal % bandage[0] == 0:
                    answer = health_calc(answer, health, bandage[2] + bandage[1])
                    cumm_heal = 0
                else:
                    answer = health_calc(answer, health, bandage[1])

        last_time = attack_time

    return answer


def health_calc(cur_health, max_health, heal):
    if cur_health + heal <= max_health:
        return cur_health + heal
    else:
        return max_health
