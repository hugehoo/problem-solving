# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         if n == 0: return
#         len1 = len(nums1)
#         end_idx = len1 - 1
#         while n > 0 and m > 0:
#             if nums2[n - 1] >= nums1[m - 1]:
#                 nums1[end_idx] = nums2[n - 1]
#                 n -= 1
#             else:
#                 nums1[end_idx] = nums1[m - 1]
#                 m -= 1
#             end_idx -= 1
#         print(nums1)
#         while n > 0:
#             nums1[end_idx] = nums2[n - 1]
#             n -= 1
#             end_idx -= 1
#         return nums1
#
#
# s = Solution()
# print(s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
# # INFP

import json
import boto3


def lambda_handler(event, context):
    # EC2 인스턴스 ID
    instance_id = 'i-069a7dfff4dd74e9d'
    print("Starting EC2 command execution")
    
    # AWS EC2 클라이언트 생성
    ec2 = boto3.client('ec2')
    print("here")
    
    # EC2 인스턴스에 명령어 실행
    ssm_client = boto3.client('ssm')
    print("here2")
    try:
        # AWS SSM client
        ssm_client = boto3.client('ssm')
        print("here2")
        
        response = ssm_client.send_command(
            InstanceIds=[instance_id],
            DocumentName='AWS-RunShellScript',
            Parameters={
                'commands': [
                    'docker pull tbnsok/guitar4u'
                ]
            }
        )
        
        print("SSM command response: ", response)
        
        command_id = response['Command']['CommandId']
        
        # Optionally, wait for the command to complete
        invocation_response = ssm_client.get_command_invocation(
            CommandId=command_id,
            InstanceId=instance_id,
        )
        
        print("Command invocation response: ", invocation_response)
        print("here3")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Docker image pull command sent to EC2 instance')
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal server error: {str(e)}")
        }
