
layui.define(['layer'], function(exports) {
    var $ = layui.jquery,
        layer = layui.layer;

    var app = {
        dialogOpen: function (options) {
                var defaults = {
                    id: null,
                    title: '系统窗口',
                    width: "800px",
                    height: "400px",
                    btnAlign: 'rt',
                    url: '',
                    maxmin: false,
                    shade: 0.3,
                    btn: ['保存'],
                    callBack: null,
                    full: false,
                    enterKey: false,
                    escKey: false,
                    type: 2
                }, that = this;
                var options = $.extend(defaults, options);
                var _url = options.url;
                var _width = that.windowWidth() > parseInt(options.width.replace('px', '')) ? options.width : that.windowWidth() + 'px';
                var _height = that.windowHeight() > parseInt(options.height.replace('px', '')) ? options.height : that.windowHeight() + 'px';
                var index = layer.open({
                    id: options.id,
                    type: options.type,
                    shade: options.shade,
                    title: options.title,
                    maxmin: options.maxmin,
                    fix: false,
                    area: [_width, _height],
                    btnAlign: options.btnAlign,
                    successClose: options.successClose,
                    content: _url,
                    btn: options.btn,
                    yes: function (index, layero) {
                        options.callBack(index, layero);
                    },
                    cancel: function () {
                        if (options.cancel != undefined) {
                            options.cancel();
                        }
                        return true;
                    },
                    success: function (layero, index) {
                        if (options.enterKey) {
                            this.enterConfirm = function (event) {
                                if (event.keyCode === 13) {
                                    $(".layui-layer-btn0").click();
                                    return false;
                                }
                            };
                            $(document).on('keydown', this.enterConfirm);
                        }
                        if (options.escKey) {
                            this.escQuit = function (event) {
                                if (event.keyCode === 0x1B) {
                                    layer.close(index);
                                    return false;
                                }
                            };
                            $(document).on('keydown', this.escQuit);
                        }
                    },
                    end: function () {
                        if (options.escKey) {
                            $(document).off('keydown', this.escQuit);
                        }
                        if (options.enterKey) {
                            $(document).off('keydown', this.enterConfirm);
                        }
                    },
                    btn2: function (layero, index) {
                        if (options.btn2 != undefined) {
                            return options.btn2(layero, index);
                        } else {
                            return true;
                        }
                    },
                    btn3: function (layero, index) {
                        if (options.btn3 != undefined) {
                            return options.btn3(layero, index);
                        } else {
                            return true;
                        }
                    }
                });
                if (options.full) {
                    layer.full(index);
                }
                return index;
            },

    };
    //expotts("key",value)
    //key你懂吧？  待会在第二步就要用key值来获取var table这个对象。继而调用对象中函数
    exports('app', app);
});