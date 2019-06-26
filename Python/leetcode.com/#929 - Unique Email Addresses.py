class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueEmail = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                firstIndex = local.find('+')
                local = local[:firstIndex]
            uniqueEmail.add(local.replace('.','') + '@' + domain)
        return len(uniqueEmail)




sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
uniques = sol.numUniqueEmails(emails)
print("Uniques: ", uniques)



