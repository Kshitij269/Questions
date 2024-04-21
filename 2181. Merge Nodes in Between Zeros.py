class Solution:
	def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
		current_node = head.next
		result = new_node = ListNode(0)

		while current_node:

			current_sum = 0

			while current_node.val != 0:
				current_sum += current_node.val
				current_node = current_node.next

			new_node.next = ListNode(current_sum)
			new_node = new_node.next

			current_node = current_node.next

		return result.next