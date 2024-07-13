# Define the configuration dictionary
SCRAPER_CONFIG = {
    'https://www.fcnb.ca/en/news-alerts': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'views-row',
            'title_tag': 'div', 'title_class': 'article__node-title',
            'date_tag': 'div', 'date_class': 'article__node-post-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': ''
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://ccua.com/ccua-news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'grid-item',
            'title_tag': 'div', 'title_class': 'inner-content-title',
            'date_tag': 'div', 'date_class': 'date',
            'link_tag': 'a', 'link_class': 'btn button button--primary',
            'error_tag': '', 'error_class': ''
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.central1.com/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'col-12',
            'title_tag': 'h2', 'title_class': 'entry-title',
            'date_tag': 'time', 'date_class': 'entry-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': ''
        },
        'pagination_info': {
            'url_template': 'https://www.central1.com/news/page/{page_number}/',
            'limit_pages': 5
        }
    },
    'https://ocuf.org/category/news/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'et_pb_post',
            'title_tag': 'h2', 'title_class': 'entry-title',
            'date_tag': 'span', 'date_class': 'published',
            'link_tag': 'a', 'link_class': '',
            'error_tag': 'h1', 'error_class': 'not-found-title' 
        },
        'pagination_info': {
            'url_template': 'https://ocuf.org/category/news/page/{page_number}/',
            'limit_pages': 5
        }
    },
    'https://www.adjalacu.com/node/13': {
        'elements_info': {
            'element_tag': 'h3', 'element_class': '',
            'title_tag': 'strong', 'title_class': '',
            'date_tag': 'span', 'date_class': 'published',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        }
    },
    'https://www.alterna.ca/en/about-us/news/': {
        'elements_info': {
            'element_tag': 'tr', 'element_class': '',
            'title_tag': 'a', 'title_class': '',
            'date_tag': 'td', 'date_class': 'description',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.alterna.ca/en/about-us/news?page={page_number}',
            'limit_pages': 5
        }
    },
    'https://bcufinancial.com/category/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'news',
            'title_tag': 'h2', 'title_class': '',
            'date_tag': 'p', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://bcufinancial.com/category/news/page/{page_number}/',
            'limit_pages': 5
        }
    },
    'https://www.duca.com/about-us/news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'post',
            'title_tag': 'h3', 'title_class': 'entry-title',
            'date_tag': 'div', 'date_class': 'entry-meta',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 5
        }
    },
    'https://www.dundalkcu.ca/about-us/whats-new/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'post',
            'title_tag': 'h3', 'title_class': 'entry-title',
            'date_tag': 'div', 'date_class': 'entry-meta',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 2
        }
    },
    'https://equitycu.com/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'x-div',
            'title_tag': 'div', 'title_class': 'x-text-headline',
            'date_tag': 'div', 'date_class': 'x-content',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.firstontario.com/media': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'big', 'title_class': '',
            'date_tag': 'a', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://ghcu.ca/whats-new/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'elementor-post',
            'title_tag': 'a', 'title_class': '',
            'date_tag': 'div', 'date_class': 'elementor-post__meta-data',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.kindredcu.com/whats-new/press-releases': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'richtext-content',
            'title_tag': 'a', 'title_class': '',
            'date_tag': 'p', 'date_class': 'font-bold',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://kccu.ca/content/latest-news': {
        'elements_info': {
            'element_tag': 'p', 'element_class': '',
            'title_tag': 'a', 'title_class': '',
            'date_tag': 'strong', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://liunalocal183.ca/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'gb-block-post-grid-text',
            'title_tag': 'a', 'title_class': '',
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.libro.ca/about/media-centre/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'a', 'title_class': '',
            'date_tag': 'li', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.dundalkcu.ca/about-us/whats-new/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://luminusfinancial.com/category/member-news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'ee-post-wrap',
            'title_tag': 'h3', 'title_class': 'ee-post-title',
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': 'breakdance-link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://luminusfinancial.com/category/member-news/page/{page_number}/',
            'limit_pages': 2
        }
    },
    'https://www.mainstreetcu.ca/news/updates': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'col-md-10',
            'title_tag': 'h3', 'title_class': '',
            'date_tag': 'p', 'date_class': '',
            'link_tag': 'a', 'link_class': 'buttonStyled',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://luminusfinancial.com/category/member-news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.itv.com/news/meridian': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'mhohf',
            'title_tag': 'a', 'title_class': 'E2VG5',
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': 'E2VG5',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://luminusfinancial.com/category/member-news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://momentumcu.ca/category/news/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'slide-entry',
            'title_tag': 'h3', 'title_class': 'slide-entry-title',
            'date_tag': 'time', 'date_class': 'slide-meta-time',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 4
        }
    },
    'https://www.mcccu.com/about-us/media': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'richtext-content',
            'title_tag': 'p', 'title_class': '',
            'date_tag': 'span', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://moyafinancial.ca/news-and-events/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'vc_grid-item',
            'title_tag': 'a', 'title_class': 'vc_gitem-link',
            'date_tag': 'a', 'date_class': 'vc_gitem-link',
            'link_tag': 'a', 'link_class': 'vc_gitem-link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.northerncu.com/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'proportional-content-margin',
            'title_tag': 'a', 'title_class': '',
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://oppa.ca/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.penfinancial.com/about/news-media': {
        'elements_info': {
            'element_tag': 'tr', 'element_class': '',
            'title_tag': 'strong', 'title_class': '', 
            'date_tag': 'td', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.rapportcu.ca/Personal/AboutUs/MediaCentre/': {
        'elements_info': {
            'element_tag': 'h2', 'element_class': 'newsevents-entry',
            'title_tag': 'span', 'title_class': 'newsevents-title', 
            'date_tag': 'span', 'date_class': 'newsevents-date',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.polcu.com/about-us/member-news': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'strong', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.central1.com/news/taiwanese-canadian-toronto-credit-union-a-pillar-of-prosperity-in-the-community/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'marg-bottom-15',
            'title_tag': 'h5', 'title_class': 'dark-blue-text', 
            'date_tag': 'p', 'date_class': 'marg-bottom-10',
            'link_tag': 'a', 'link_class': 'blue-text-link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://talka.ca/blog/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'elementor-post__text',
            'title_tag': 'h3', 'title_class': 'elementor-post__title', 
            'date_tag': 'span', 'date_class': 'elementor-post-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.tandia.com/about-us/Media/Tandia-news-and-media': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'richtext-content',
            'title_tag': 'h5', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': 'primary',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://theenergycu.com/category/energy-news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'mk-blog-meta',
            'title_tag': 'h3', 'title_class': 'the-title', 
            'date_tag': 'time', 'date_class': '',
            'link_tag': 'a', 'link_class': 'mk-readmore',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.thepolicecu.org/news': {
        'elements_info': {
            'element_tag': 'p', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'a', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.yncu.com/about/media-centre': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'component-collapsible-content',
            'title_tag': 'div', 'title_class': 'collapsible-content-header', 
            'date_tag': 'div', 'date_class': 'collapsible-content-body',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.fintechfutures.com/2024/05/beem-credit-union-teams-up-with-veripark-to-elevate-digital-banking-capabilities/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'single-post-content',
            'title_tag': 'h1', 'title_class': 'single-post-content_title', 
            'date_tag': 'li', 'date_class': 'byline',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.bvcu.com/Community/Member-news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'richtext-content',
            'title_tag': 'h3', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': 'primary',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.axiommutual.ca/name-change/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'row',
            'title_tag': 'p', 'title_class': 'has-large-font-size', 
            'date_tag': 'p', 'date_class': 'font-weight-bold',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.coastcapitalsavings.com/about-us/press-room/news-releases/2023': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'col-12 news-content',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'div', 'date_class': 'news-list-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://momentumcu.ca/category/news/page/{page_number}/',
            'limit_pages': 1
        }
    },
    'https://www.ayrmutual.com/site/blog': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'entry-content',
            'title_tag': 'h2', 'title_class': 'title', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.ayrmutual.com/site/blog/page/{page_number}',
            'limit_pages': 5
        }
    },
    'https://www.cccu.ca/about/member-news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'richtext-content',
            'title_tag': 'h4', 'title_class': '', 
            'date_tag': 'p', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.ayrmutual.com/site/blog/page/{page_number}',
            'limit_pages': 5
        }
    },
    'https://bayofquintemutual.com/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'column small-12 medium-6 large-4 blog',
            'title_tag': 'h3', 'title_class': '', 
            'date_tag': 'p', 'date_class': 'date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://bayofquintemutual.com/news/page/{page_number}/',
            'limit_pages': 5
        }
    },
    'https://www.cvcu.bc.ca/cvcu-news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'component-article',
            'title_tag': 'h4', 'title_class': 'simple-info-card-title proportional-content-margin', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '',
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://bcminsurance.com/category/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'fusion-post-content post-content',
            'title_tag': 'h2', 'title_class': 'fusion-post-title fusion-responsive-typography-calculated', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.caainsurancecompany.ca/media': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'spotlight-item',
            'title_tag': 'h3', 'title_class': '', 
            'date_tag': 'time', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.desjardins.com/ca/your-credit-union/ontario/index.jsp': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'cd-33',
            'title_tag': 'h2', 'title_class': 'cd-style-h5', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.ctmins.ca/news/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'elementor-post elementor-grid-item post-5902 post type-post status-publish format-standard hentry category-uncategorized',
            'title_tag': 'h3', 'title_class': 'elementor-post__title', 
            'date_tag': 'span', 'date_class': 'elementor-post-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.comtechfirecu.com/Personal/AboutUs/MediaCentre/Updates/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'Component-StandardContent',
            'title_tag': 'h2', 'title_class': '', 
            'date_tag': 'h2', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.cayugamutual.com/category/in-the-news/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'fusion-post-large',
            'title_tag': 'h2', 'title_class': 'entry-title', 
            'date_tag': 'span', 'date_class': 'updated rich-snippet-hidden',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.firstcu.ca/our-difference/news-and-events/news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'richtext-content',
            'title_tag': 'h3', 'title_class': '', 
            'date_tag': 'strong', 'date_class': '',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.firstwestcu.ca/media/fwcu/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'css-grid__item',
            'title_tag': 'h3', 'title_class': 'media-release__title', 
            'date_tag': 'p', 'date_class': 'media-release__date',
            'link_tag': 'a', 'link_class': 'read-more',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://curie.org/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'elementor-post',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'elementor-post-date',
            'link_tag': 'a', 'link_class': 'elementor-post__read-more',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.gulfandfraser.com/about-us/member-news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'layout-grid-item',
            'title_tag': 'h4', 'title_class': 'simple-info-card-title', 
            'date_tag': 'div', 'date_class': 'subheading',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.gvccu.com/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'layout-grid-item',
            'title_tag': 'h5', 'title_class': 'simple-info-card-title', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://dumfriesmutual.com/client-centre/blog/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': 'no-img',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.edgemutual.com/about/in-the-news/category/locally/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'item-meta',
            'title_tag': 'h3', 'title_class': 'item-title', 
            'date_tag': 'time', 'date_class': 'item-published',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://fortyork.com/news/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': 'fusion-layout-column',
            'title_tag': 'a', 'title_class': 'awb-custom-text-color', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': 'awb-custom-text-color',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.integriscu.ca/category/blog/about/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'entry-content-wrap',
            'title_tag': 'h2', 'title_class': 'entry-title', 
            'date_tag': 'span', 'date_class': 'posted-on',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.integriscu.ca/category/blog/about/news/page/{page_number}/',
            'limit_pages': 2
        }
    },
    'https://www.eriemutual.com/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'content',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'span', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.integriscu.ca/category/blog/about/news/page/{page_number}/',
            'limit_pages': 2
        }
    },
    'https://otlablog.com/fraser-v-fenchurch-general-insurance-2022-onsc-6222/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'blog-post',
            'title_tag': 'h1', 'title_class': 'post-title', 
            'date_tag': 'div', 'date_class': 'entry-meta',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 2
        }
    },
    'https://www.khalsacreditunion.ca/about/membership-news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'col-md-12',
            'title_tag': 'h5', 'title_class': 'pb-3', 
            'date_tag': 'h5', 'date_class': 'pb-3',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.hmecu.com/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'content',
            'title_tag': 'h3', 'title_class': 'simple-info-card-title', 
            'date_tag': 'div', 'date_class': 'subheading',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.ldcu.ca/Personal/AboutUs/MediaCenter/PressReleases/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'LDCUNews',
            'title_tag': 'p', 'title_class': 'readMore', 
            'date_tag': 'p', 'date_class': '',
            'link_tag': 'a', 'link_class': 'LDCUreadMore',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.osfi-bsif.gc.ca/en/news?type=5': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'content',
            'title_tag': 'a', 'title_class': 'title--link', 
            'date_tag': 'time', 'date_class': '',
            'link_tag': 'a', 'link_class': 'title--link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.bis.org/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': 'singlelink',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.osc.ca/en/news-events': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'carousel-card__content',
            'title_tag': 'a', 'title_class': 'title', 
            'date_tag': 'time', 'date_class': 'datetime',
            'link_tag': 'a', 'link_class': 'title',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.federalreserve.gov/newsevents.htm': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'news__item',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'p', 'date_class': 'time--sm',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.coalitioninc.com/en-ca/newsroom': {
        'elements_info': {
            'element_tag': 'a', 'element_class': 'MuiTypography-root',
            'title_tag': 'div', 'title_class': 'css-16y7pky-Text-richSubtitle', 
            'date_tag': 'b', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.coalitioninc.com/en-ca/newsroom?page={page_number}',
            'limit_pages': 5
        }
    },
    'https://www.coastcapitalsavings.com/about-us/press-room': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'latest-news-content',
            'title_tag': 'div', 'title_class': 'latest-news-title', 
            'date_tag': 'div', 'date_class': 'latest-news-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.ttc.ca/news': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'div', 'date_class': 'c-news-results__date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://dyedurham.com/media/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'post-card',
            'title_tag': 'h3', 'title_class': 'post-card__heading', 
            'date_tag': 'div', 'date_class': 'post-card__date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.gov.nl.ca/releases/r/?ndept=DGSNL': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'span', 'title_class': 'title', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.vancity.com/AboutVancity/News/': {
        'elements_info': {
            'element_tag': 'p', 'element_class': '',
            'title_tag': 'a', 'title_class': 'notcurrent', 
            'date_tag': 'b', 'date_class': '',
            'link_tag': 'a', 'link_class': 'notcurrent',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.prospera.ca/About/Press+releases': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'content',
            'title_tag': 'h3', 'title_class': 'simple-info-card-title', 
            'date_tag': 'div', 'date_class': 'subheading',
            'link_tag': 'a', 'link_class': 'secondary',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.gov.nt.ca/en/newsroom': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'views-row',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'field-content',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://secure3.mearie.ca/reciprocal-news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'postEntry',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.fsb.org/press/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'media-body',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'media-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.togetherwearebetter.ca/media/': {
        'elements_info': {
            'element_tag': 'p', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'strong', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.iosco.org/media_room/?subsection=media_releases': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'strong', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'http://www.tctcu.com/?menuid=14431&lgid=1&siteid=100620': {
        'elements_info': {
            'element_tag': 'ul', 'element_class': 'listing-ul',
            'title_tag': 'li', 'title_class': 'upc-subject', 
            'date_tag': 'li', 'date_class': 'upc-date',
            'link_tag': 'a', 'link_class': 'bodylink',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.ncino.com/news/newsroom-home?tab=pressReleases': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'group/card',
            'title_tag': 'a', 'title_class': 'line-clamp-4', 
            'date_tag': 'p', 'date_class': 'text-navy-700',
            'link_tag': 'a', 'link_class': 'line-clamp-4',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.mainstreetcu.ca/news/updates': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'col-md-10',
            'title_tag': 'h3', 'title_class': '', 
            'date_tag': 'p', 'date_class': '',
            'link_tag': 'a', 'link_class': 'buttonStyled',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://celero.ca/news-releases/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'p-info',
            'title_tag': 'h3', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'p-topline',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://news.novascotia.ca/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'recent-news-horizontal--info',
            'title_tag': 'span', 'title_class': 'field-content', 
            'date_tag': 'time', 'date_class': 'datetime',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.cgi.com/en/press-releases/2024': {
        'elements_info': {
            'element_tag': 'tr', 'element_class': '',
            'title_tag': 'td', 'title_class': 'views-field-title', 
            'date_tag': 'td', 'date_class': 'views-field-created',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://asic.gov.au/newsroom/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'a', 'title_class': 'nh-list-link', 
            'date_tag': 'span', 'date_class': 'nh-list-date',
            'link_tag': 'a', 'link_class': 'nh-list-link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.bcfsa.ca/about-us/news?search=&page=0#search-results': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'g-teaser',
            'title_tag': 'a', 'title_class': 'g-link', 
            'date_tag': 'time', 'date_class': 'g-teaser__date',
            'link_tag': 'a', 'link_class': 'g-link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.northerncu.com/about/media-centre': {
        'elements_info': {
            'element_tag': 'tr', 'element_class': '',
            'title_tag': 'td', 'title_class': '', 
            'date_tag': 'td', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://coop.desjardins.com/ca/your-credit-union/ontario/events/index.jsp': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'nowrap',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1,
            'pages_xpaths': ['/html/body/div[6]/div[2]/div/div/div[2]/div/button[2]', 
                             '/html/body/div[4]/div[1]/div[2]/form/div[3]/button']
        }
    },
    'https://www.desjardins.com/on/en/news.html': {
        'elements_info': {
            'element_tag': 'article', 'element_class': '',
            'title_tag': 'span', 'title_class': 'cmp-list__item-link-text', 
            'date_tag': 'span', 'date_class': 'cmp-list__item-date',
            'link_tag': 'a', 'link_class': 'cmp-list__item-link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.desjardins.com/qc/en/news.html?page={page_number}',
            'limit_pages': 2,
            'pages_xpaths': ['/html/body/div[6]/div[2]/div/div/div[2]/div/button[2]', 
                             '/html/body/div[4]/div[1]/div[2]/form/div[3]/button']
        }
    },
    
    'https://www.fca.org.uk/news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'content-list-item',
            'title_tag': 'span', 'title_class': 'content-item__title', 
            'date_tag': 'time', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.desjardins.com/qc/en/news.html?page={page_number}',
            'limit_pages': 1,
        }
    },
    'https://www.securities-administrators.ca/news/': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'listing-item',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'time', 'date_class': 'entry-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.desjardins.com/qc/en/news.html?page={page_number}',
            'limit_pages': 1,
        }
    },
    'https://www.marsh.com/ca/en/about/media.html': {
        'elements_info': {
            'element_tag': 'a', 'element_class': 'c-content-card__content-link',
            'title_tag': 'h3', 'title_class': 'c-content-card__title', 
            'date_tag': 'p', 'date_class': 'c-content-card__date',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://www.desjardins.com/qc/en/news.html?page={page_number}',
            'limit_pages': 1,
        }
    },
    'https://www.lakeviewcreditunion.com/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'content',
            'title_tag': 'h4', 'title_class': 'simple-info-card-title', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.cfc.com/en-gb/knowledge/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'knowledge-content-listings-with-filters__articles-item',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'knowledge-content-listings-with-filters__articles-item-details-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://news.ontario.ca/en': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'row',
            'title_tag': 'a', 'title_class': 'a_no_line', 
            'date_tag': 'p', 'date_class': 'feature_date',
            'link_tag': 'a', 'link_class': 'a_no_line',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.beazley.com/en-CA/news-and-events/': {
        'elements_info': {
            'element_tag': 'a', 'element_class': 'js-card',
            'title_tag': 'h4', 'title_class': 'line-clamp-3', 
            'date_tag': '', 'date_class': '',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.cipf.ca/news-publications': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'list-content',
            'title_tag': 'h3', 'title_class': '', 
            'date_tag': 'div', 'date_class': 'text-muted',
            'link_tag': 'a', 'link_class': 'btn',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.insurance-canada.ca/hot/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'div', 'date_class': 'rpwwt-post-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.sec.gov/newsroom': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'view-content',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'time', 'date_class': 'datetime',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://newsroom.fiserv.com/newsroom': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'clearfix',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'div', 'date_class': 'news-date-column',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx': {
        'elements_info': {
            'element_tag': 'tr', 'element_class': '',
            'title_tag': 'a', 'title_class': 'link2', 
            'date_tag': 'a', 'date_class': 'link2',
            'link_tag': 'a', 'link_class': 'link2',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.blueshorefinancial.com/about-blueshore/news-events/news': {
        'elements_info': {
            'element_tag': '', 'element_class': '',
            'title_tag': '', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.blueshorefinancial.com/about-blueshore/news-events/news': {
        'elements_info': {
            'element_tag': '', 'element_class': '',
            'title_tag': '', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.mas.gov.sg/news': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'mas-search-card',
            'title_tag': 'a', 'title_class': 'ola-btn', 
            'date_tag': 'div', 'date_class': 'ts:xs',
            'link_tag': 'a', 'link_class': 'ola-btn',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.vantageone.net/blog/': {
        'elements_info': {
            'element_tag': 'a', 'element_class': 'av-masonry-entry',
            'title_tag': 'h3', 'title_class': 'av-masonry-entry-title entry-title', 
            'date_tag': 'span', 'date_class': 'av-masonry-date',
            'link_tag': '', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://apps.sfc.hk/edistributionWeb/gateway/EN/news-and-announcements/news/': {
        'elements_info': {
            'element_tag': 'tr', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'td', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://lautorite.qc.ca/en/general-public/media-centre/news': {
        'elements_info': {
            'element_tag': 'li', 'element_class': 'search-result',
            'title_tag': 'a', 'title_class': 'search-result-title', 
            'date_tag': 'span', 'date_class': 'search-result-date',
            'link_tag': 'a', 'link_class': 'search-result-title',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.esma.europa.eu/press-news/esma-news': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'node--type-news',
            'title_tag': 'div', 'title_class': 'search-title', 
            'date_tag': 'div', 'date_class': 'search-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.ngfs.net/en/news/communique-de-presse': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'node-communique-de-presse',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.fsrao.ca/newsroom': {
        'elements_info': {
            'element_tag': 'article', 'element_class': 'node--type-article',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'time', 'date_class': 'datetime',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://news.na.chubb.com/canada': {
        'elements_info': {
            'element_tag': 'li', 'element_class': 'wd_item',
            'title_tag': 'div', 'title_class': 'wd_title', 
            'date_tag': 'div', 'date_class': 'wd_date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': 'https://news.na.chubb.com/canada?o={page_number}',
            'limit_pages': 1
        }
    },
    'https://kcccu.ca/announcements/': {
        'elements_info': {
            'element_tag': 'td', 'element_class': 'webzine-item-box',
            'title_tag': 'div', 'title_class': 'webzine-item-title', 
            'date_tag': 'span', 'date_class': 'info-date',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.insurance-canada.ca/tag/hamilton-township-mutual/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': 'post',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': 'time', 'date_class': 'updated',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://npscu.ca/about/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'category-press-release',
            'title_tag': 'h2', 'title_class': 'entry__title card__title h5', 
            'date_tag': 'span', 'date_class': 'entry__meta__item entry__date',
            'link_tag': 'a', 'link_class': 'card card--link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.hiroc.com/news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'column l-two-third',
            'title_tag': 'span', 'title_class': 'field-name--title', 
            'date_tag': 'time', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://ocubc.com/category/news-events/': {
        'elements_info': {
            'element_tag': 'h2', 'element_class': 'entry-title',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.kemutual.com/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'content-wrapper',
            'title_tag': 'h3', 'title_class': '', 
            'date_tag': 'time', 'date_class': '',
            'link_tag': 'a', 'link_class': 'post-link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.prospera.ca/About/2022+Press+releases': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'content',
            'title_tag': 'h3', 'title_class': 'simple-info-card-title', 
            'date_tag': 'div', 'date_class': 'subheading',
            'link_tag': 'a', 'link_class': 'secondary',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.lawpro.ca/about/news/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': '',
            'title_tag': 'a', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': 'secondary',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.sharons.ca/about-scu/about_intro/news': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'iw_placeholder',
            'title_tag': 'strong', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://maplemutual.com/': {
        'elements_info': {
            'element_tag': 'strong', 'element_class': '',
            'title_tag': 'h3', 'title_class': 'h-recent-posts', 
            'date_tag': 'span', 'date_class': 'x-recent-posts-date',
            'link_tag': 'a', 'link_class': 'x-recent-post2',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.maxlifeinsurance.com/newsroom': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'media-box',
            'title_tag': 'p', 'title_class': '', 
            'date_tag': 'span', 'date_class': 'flr assetNewsDate',
            'link_tag': 'a', 'link_class': 'aligned-button',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.sdcu.com/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'component-c1-simple-info-card',
            'title_tag': 'h2', 'title_class': 'simple-info-card-title', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://gocognition.com/press-release/htm-insurance-mckillop-mutual-go-live-cognition-claims-solution/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'post-item-wrapper',
            'title_tag': 'h4', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.vancity.com/viewport/mobile/AboutVancity/News/': {
        'elements_info': {
            'element_tag': 'p', 'element_class': '',
            'title_tag': 'a', 'title_class': 'notcurrent', 
            'date_tag': 'b', 'date_class': '',
            'link_tag': 'a', 'link_class': 'notcurrent',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://novamutual.com/news/': {
        'elements_info': {
            'element_tag': 'a', 'element_class': 'newsItemClass',
            'title_tag': 'p', 'title_class': 'text-indigo', 
            'date_tag': 'p', 'date_class': 'text-charcoal',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.northernbirchcu.com/community/news-events': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'richtext-content',
            'title_tag': 'p', 'title_class': '', 
            'date_tag': '', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.vantageone.net/home/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': 'news-content',
            'title_tag': 'strong', 'title_class': "news-headline", 
            'date_tag': 'span', 'date_class': 'news-time',
            'link_tag': 'a', 'link_class': 'news-link',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.wldcu.com/en/home/news-and-alerts': {
        'elements_info': {
            'element_tag': 'tr', 'element_class': '',
            'title_tag': 'td', 'title_class': "link", 
            'date_tag': 'td', 'date_class': 'description',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.osbie.on.ca/': {
        'elements_info': {
            'element_tag': 'a', 'element_class': 'cta--card',
            'title_tag': 'h3', 'title_class': "cta__heading", 
            'date_tag': 'p', 'date_class': 'text-teal',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.peelmutual.com/news/': {
        'elements_info': {
            'element_tag': 'li', 'element_class': 'wp-block-post',
            'title_tag': 'h3', 'title_class': "nfd-text-lg", 
            'date_tag': 'time', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://prodemnity.com/news-views/': {
        'elements_info': {
            'element_tag': 'header', 'element_class': 'wp-block-getwid-recent-posts__entry-header',
            'title_tag': 'a', 'title_class': "", 
            'date_tag': 'time', 'date_class': '',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.salusmutual.ca/news/': {
        'elements_info': {
            'element_tag': 'div', 'element_class': 'item-meta',
            'title_tag': 'h3', 'title_class': "item-title", 
            'date_tag': 'time', 'date_class': 'item-published',
            'link_tag': 'a', 'link_class': '',
            'error_tag': '', 'error_class': '' 
        },
        'pagination_info': {
            'url_template': '',
            'limit_pages': 1
        }
    },
    'https://www.sgicanada.org/news/sgi-canada-newsletter': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'article',
                'title_tag': 'div', 'title_class': "post-copy", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'more',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
    'https://www.southeasthope.com/blog/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'article',
                'title_tag': 'h2', 'title_class': "article--title", 
                'date_tag': 'li', 'date_class': 'article--meta_item -date',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
    'https://www.insideottawavalley.com/news/smiths-falls-community-credit-union-is-first-to-launch-paperless-processing/article_01b2c031-0cf3-5174-afbf-143b8d849c53.html': {
            'elements_info': {
                'element_tag': 'article', 'element_class': 'tnt-section-news',
                'title_tag': 'h3', 'title_class': "tnt-headline", 
                'date_tag': 'time', 'date_class': 'tnt-date tnt-update-recent asset-date text-muted',
                'link_tag': 'a', 'link_class': 'tnt-asset-link',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },  
    'https://gocognition.com/press-release/west-wawanosh-mutual-continues-digital-transformation-implementing-cognition-underwriting/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'post-item-wrapper',
                'title_tag': 'h4', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },    
    'https://www.wfcu.ca/Personal/AboutUs/MediaCentre/LatestNews/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'post-content',
                'title_tag': 'div', 'title_class': "content-inner", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'entire-meta-link',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },   
     'https://amico.ca/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'content-block',
                'title_tag': 'h3', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },    
     'https://www.blueshorefinancial.com/about-blueshore/news-events': {
            'elements_info': {
                'element_tag': 'body', 'element_class': '',
                'title_tag': 'h2', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
      'https://www.farmmutualre.com/portfolio-item/amherst-island-mutual-insurance-company/': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },   
      'https://hellocu.com/special-offers-and-announcements/bay-credit-union-merger': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'rich-text w-richtext',
                'title_tag': 'h2', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
        
       'https://www.comsavings.com/working-together': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'richtext-content',
                'title_tag': 'h3', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },  
       'https://www.brantmutual.com/news/announcements/welcome-to-our-new-website/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'fl-builder-content',
                'title_tag': 'h1', 'title_class': "uabb-heading", 
                'date_tag': 'div', 'date_class': 'fl-html',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },  
        'https://www.caissealliance.com/en/faq/how-can-we-remain-well-informed-about-your-latest-news/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },     
        'https://www.cecu.ca/blog/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'clsPost',
                'title_tag': 'div', 'title_class': "clsTitle", 
                'date_tag': 'div', 'date_class': 'clsDate',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.cdcu.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'cta-text-content',
                'title_tag': 'h3', 'title_class': "cta-heading", 
                'date_tag': 'div', 'date_class': 'clsDate',
                'link_tag': 'a', 'link_class': 'primary',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
        'https://www.firstwestcu.ca/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'intro-block',
                'title_tag': 'h2', 'title_class': "copy-block__title", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'button--primary',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
        'https://www.copperfin.ca/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'icon-info-card-text-content',
                'title_tag': 'h2', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
        'https://secure3.mearie.ca/reciprocal-news/safeguarding-your-reciprocal': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'title-and-featured-image-block',
                'title_tag': 'span', 'title_class': "hs_cos_wrapper", 
                'date_tag': 'span', 'date_class': 'post-meta',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },     
        'https://www.coachmaninsurance.ca/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'newslinks',
                'title_tag': 'a', 'title_class': "newsred", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'newsred',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://dufferinmutual.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'wp-block-group__inner-container',
                'title_tag': 'h2', 'title_class': "wp-block-heading", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'wp-block-button__link',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
        'https://www.finnishcu.com/index.php?command=news_30': {
            'elements_info': {
                'element_tag': 'li', 'element_class': '',
                'title_tag': 'span', 'title_class': "subtitle", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.frontlinecu.com/assets/pdfs/Spring2021_newsletter.pdf': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },  
        'https://www.interiorsavings.com/about-us/news-and-events/gulf-and-fraser-merger': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'component-title-with-copy',
                'title_tag': 'h1', 'title_class': "title", 
                'date_tag': 'strong', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
        'https://online.ganaraskacu.com/Personal/AboutUs/MediaCentre/PressReleases/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'mainContent',
                'title_tag': 'h1', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.farmmutualre.com/': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.germaniamutual.com/g/newsletter/': {
            'elements_info': {
                'element_tag': 'p', 'element_class': '',
                'title_tag': 'a', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.kscu.com/about-us/latest-news': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'component-collapsible-content',
                'title_tag': 'span', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://gfd.org/': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
       'https://www.icsavings.ca/whats-new/news-updates': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'content',
                'title_tag': 'h3', 'title_class': "simple-info-card-title", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'link',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },   

        'https://www.grenvillemutual.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'elementor-element',
                'title_tag': 'h4', 'title_class': "elementor-heading-title", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'elementor-button',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.kawarthacu.com/home': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'content',
                'title_tag': 'h4', 'title_class': "simple-info-card-title", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'link',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
       'https://www.halwellmutual.com/category/news/': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },  
        'https://www.nelsoncu.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'content',
                'title_tag': 'a', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.fsrao.ca/credit-unions/korean-toronto-credit-union-limited': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'region--content',
                'title_tag': 'span', 'title_class': "field--name-title", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
       'https://www.northsave.com/about/member-news': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'iw_component',
                'title_tag': 'h2', 'title_class': "title", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
        'https://www.howickmutual.com/Modules/News/en': {
            'elements_info': {
                'element_tag': 'li', 'element_class': '',
                'title_tag': 'span', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },  
        'https://kcccu.ca/': {
            'elements_info': {
                'element_tag': 'td', 'element_class': 'mb-latest-item-title',
                'title_tag': 'span', 'title_class': "mb-latest-item-title-text", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        }, 
        'https://l-amutual.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'fusion-text',
                'title_tag': 'strong', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'fusion-button',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.revcu.com/about-us/news-media': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'richtext-content',
                'title_tag': 'span', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': 'fusion-button',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.lambtonmutual.com/announcements/announcement-5/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'richtext-content',
                'title_tag': 'span', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': 'fusion-button',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.dailyitem.com/wire/business/northeast-credit-union-undergoes-a-rebrand-emerging-as-lighthouse-credit-union/article_7556d91e-362b-5a40-bbf3-4a4c6a2f47eb.html': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.sascu.com/about/community/news-and-events': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'content',
                'title_tag': 'h4', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.stellervista.com/about/who-we-are/news': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'richtext-content',
                'title_tag': 'strong', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.sunshineccu.com/about/member-news': {
            'elements_info': {
                'element_tag': 'li', 'element_class': '',
                'title_tag': 'a', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.valleyfirst.com/media': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'cta-text-content',
                'title_tag': 'h3', 'title_class': "cta-heading", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'primary',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.middlesexmutual.on.ca/Modules/News/Search.aspx?feedID=1e89eff9-b3a0-4353-bf2b-8b942303b295': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.northblenheim.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'comp-lnp5sf5p wixui-rich-text',
                'title_tag': 'span', 'title_class': "wixui-rich-text__text", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'uDW_Qe wixui-button',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.vanfirecu.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'et_pb_slide_description',
                'title_tag': 'h1', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'et_pb_button',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.omex.org/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'avia_textblock',
                'title_tag': 'strong', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.oecu.on.ca/': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.omia.com/intranet/Site/view.cfm?pageID=2000410': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.oshawacu.com/member-corner/stay-informed/news': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://parama.ca/news': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://piex.ca/': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.pathwise.ca/about/about-pathwise/News+and+Events': {
            'elements_info': {
                'element_tag': 'tr', 'element_class': '',
                'title_tag': 'strong', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        
        'https://www.rpcul.com/about-us/news': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'cta-text-content',
                'title_tag': 'h2', 'title_class': "cta-heading", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://thecommonwell.ca/media/': {
            'elements_info': {
                'element_tag': 'article', 'element_class': '',
                'title_tag': 'h2', 'title_class': "wp-block-heading", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://online.southwestcu.com/Personal/covid19/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'colTwo',
                'title_tag': 'h1', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.traditionmutual.com/company-updates/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'av-special-heading-h3',
                'title_tag': 'h3', 'title_class': "av-special-heading-tag", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'http://trilliummutual.com/wp-content/uploads/2020/07/CMHA-PRESS.pdf': {
            'elements_info': {
                'element_tag': '', 'element_class': '',
                'title_tag': '', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },
        'https://www.sudburycu.com/about-us/organization/latest-news': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'richtext-content',
                'title_tag': 'h3', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.ttc.ca/transparency-and-accountability/policies/Privacy/privacy-code---coach-terminal-and-insurance-company': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'richtext-content',
                'title_tag': 'h1', 'title_class': "field-title", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://usborneandhibbert.ca/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'col-md-6',
                'title_tag': 'a', 'title_class': "btn-outline-secondary", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': 'btn-outline-secondary',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://wmic.ca/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'wp-block-image',
                'title_tag': 'a', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': '', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://yarmouthmutual.com/news/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'about-new-row2-right',
                'title_tag': 'h2', 'title_class': "secondary", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.thoroldcu.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'content',
                'title_tag': 'h4', 'title_class': "simple-info-card-title", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': 'link',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.ukrainiancu.com/about-us/press-releases': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'richtext-content',
                'title_tag': 'a', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

        'https://www.yourcu.com/': {
            'elements_info': {
                'element_tag': 'div', 'element_class': 'icon-info-card-text-content',
                'title_tag': 'a', 'title_class': "", 
                'date_tag': '', 'date_class': '',
                'link_tag': 'a', 'link_class': '',
                'error_tag': '', 'error_class': '' 
            },
            'pagination_info': {
                'url_template': '',
                'limit_pages': 1
            }
        },

}