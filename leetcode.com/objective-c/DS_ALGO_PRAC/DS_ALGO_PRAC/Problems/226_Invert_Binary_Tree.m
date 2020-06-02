//
//  226_Invert_Binary_Tree.m
//  DS_ALGO_PRAC
//
//  Created by Partho Biswas on 6/2/20.
//  Copyright © 2020 Partho Biswas. All rights reserved.
//

#import "226_Invert_Binary_Tree.h"

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

@implementation _26_Invert_Binary_Tree

- (struct TreeNode *)invertTree:(struct TreeNode *)root {
    if (!root) {
        return nil;
    }
    
    struct TreeNode *left = [self invertTree:root->left];
    struct TreeNode *right = [self invertTree:root->right];
    root->left = right;
    root->right = left;
    return root;
}

@end
