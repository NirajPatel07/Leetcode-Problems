var inorderTraversal = function(root) {
    const result = [];
    
    function inorder(root){
        if (!root){
            return;
        }
        
        inorder(root.left);
        result.push(root.val);
        inorder(root.right);
    }
    
    inorder(root);
    return result;
};