var tree2str = function(root) {
    const res = [];
    
    function preorder(root) {
        if (!root){
            return;
        }
        
        res.push("(");
        res.push(root.val);
        
        if (!root.left && root.right){
            res.push("()");
        }
        
        preorder(root.left);
        preorder(root.right);
        res.push(")");
        
    }
    
    preorder(root);
    return res.slice(1, -1).join("");
};