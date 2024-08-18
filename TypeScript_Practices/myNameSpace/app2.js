#!/usr/bin/node
var usersUtils;
(function (usersUtils) {
    var Parent = /** @class */ (function () {
        function Parent() {
        }
        Parent.prototype.getstatus = function () {
            console.log("I am a parent");
        };
        return Parent;
    }());
    usersUtils.Parent = Parent;
})(usersUtils || (usersUtils = {}));
