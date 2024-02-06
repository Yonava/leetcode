/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1, m, nums2, n) {
    for (let i = m ; i < m+n; i++) {
        nums1[i] = nums2[i-m]
    }

    nums1.sort(function(a,b) { return a - b } )
};