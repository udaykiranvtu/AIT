class GoalStackPlanner:

    def __init__(self):
        # Initial state
        self.state = {
            'on_floor(Monkey)',
            'at(Monkey, Center)',
            'at(Box, Window)'
        }

        # Operators
        self.operators = {
            'Walk(Floor, Center, Window)': {
                'preconds': {
                    'on_floor(Monkey)',
                    'at(Monkey, Center)'
                },
                'add': {
                    'at(Monkey, Window)'
                },
                'del': {
                    'at(Monkey, Center)'
                }
            },

            'Push(Box, Window, Center)': {
                'preconds': {
                    'on_floor(Monkey)',
                    'at(Monkey, Window)',
                    'at(Box, Window)'
                },
                'add': {
                    'at(Monkey, Center)',
                    'at(Box, Center)'
                },
                'del': {
                    'at(Monkey, Window)',
                    'at(Box, Window)'
                }
            },

            'Climb(Box)': {
                'preconds': {
                    'on_floor(Monkey)',
                    'at(Monkey, Center)',
                    'at(Box, Center)'
                },
                'add': {
                    'on_box(Monkey)'
                },
                'del': {
                    'on_floor(Monkey)'
                }
            },

            'Grasp(Banana)': {
                'preconds': {
                    'on_box(Monkey)',
                    'at(Box, Center)',
                    'at(Monkey, Center)'
                },
                'add': {
                    'has(Monkey, Banana)'
                },
                'del': set()
            }
        }


    def apply_operator(self, name):
        """Apply an operator if all its preconditions are satisfied."""

        operator = self.operators[name]

        if operator['preconds'].issubset(self.state):

            # Remove delete-list predicates
            self.state -= operator['del']

            # Add new predicates
            self.state |= operator['add']

            return True

        return False


    def plan(self, goal):
        """Generate and execute the goal stack plan."""

        goal_stack = [goal]
        plan = []

        # Mapping goals to operators
        goal_operators = {
            'has(Monkey, Banana)': 'Grasp(Banana)',
            'on_box(Monkey)': 'Climb(Box)',
            'at(Box, Center)': 'Push(Box, Window, Center)',
            'at(Monkey, Window)': 'Walk(Floor, Center, Window)'
        }

        while goal_stack:

            current = goal_stack.pop()

            # If current goal is already achieved
            if current in self.state:
                continue

            # If current item is an operator
            if current in self.operators:

                operator = self.operators[current]

                # Check preconditions
                if operator['preconds'].issubset(self.state):
                    self.apply_operator(current)
                    plan.append(current)
                else:
                    print("Cannot execute:", current)
                    return None

            # Otherwise, current item is a goal
            elif current in goal_operators:

                operator = goal_operators[current]

                # Push operator first
                goal_stack.append(operator)

                # Push unsatisfied preconditions
                for precondition in goal_operators.get(current, []) if False else []:
                    goal_stack.append(precondition)

                # Special handling for operator preconditions
                for precondition in self.operators[operator]['preconds']:
                    if precondition not in self.state:
                        goal_stack.append(precondition)

        return plan


# ------------------------------------------------
# Main Program
# ------------------------------------------------

planner = GoalStackPlanner()

goal = 'has(Monkey, Banana)'

plan = planner.plan(goal)

if plan:
    print("Goal Stack Planning - Monkey Banana Problem")
    print("--------------------------------------------")

    print("\nSequence of Actions:")

    for i, action in enumerate(plan, 1):
        print(f"{i}. {action}")

    print("\nFinal State:")

    for state in sorted(planner.state):
        print(state)

    if goal in planner.state:
        print("\nResult: Monkey successfully obtained the banana.")
    else:
        print("\nResult: Goal could not be achieved.")