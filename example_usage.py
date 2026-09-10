from client import AgentToolCallSelfHealingRetryGuardClient

def main():
    client = AgentToolCallSelfHealingRetryGuardClient()
    res = client.repair_and_guard_tool_call()
    print('Tool Call Self-Healing: ' + res['healing_id'] + ' (' + res['self_healing_verdict'] + ')')
    print('Violations: ' + str(res['schema_violations_intercepted']) + ' | Latency Saved: ' + str(res['latency_saved_ms']) + 'ms')
    print('Healed Arguments: ' + str(res['healed_arguments_dict']))
    print('Telemetry: ' + res['guard_telemetry_url'])

if __name__ == '__main__':
    main()
