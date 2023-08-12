
class CustomRoleModel():
    '''统一自定义角色定义数据结构

    role_name: 角色名称
    persona: 角色基本信息定义
    first_message: 角色的第一句话
    personality: 角色的性格简短描述
    scenario: 角色的对话的情况和背景
    examples_of_dialogue: 角色的对话样例

    '''
    role_name: str
    persona: str
    first_message: str
    personality: str
    scenario: str
    examples_of_dialogue: str

    def __init__(self, role_name: str, persona: str, first_message: str, personality: str, scenario: str, examples_of_dialogue) -> None:
        self.role_name = role_name
        self.persona = persona
        self.first_message = first_message
        self.personality = personality
        self.scenario = scenario
        self.examples_of_dialogue = examples_of_dialogue