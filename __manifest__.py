{
    'name': "Online-Courses Management",

    'summary': """Create Online Courses""",

    'description': """
        The Online Courses Management Module is a comprehensive solution designed to streamline online learning.
        It enables educators to create, organize, and manage courses with ease, including lessons and attachments,
        while facilitating seamless attendee registration. With its intuitive interface,
        the module enhances the teaching experience and provides an engaging platform for learners to thrive.

        Developed by LINABOUI Ali, AKKAOUI Hamza.
    """,

    'author': "Ali LINABOUI , Hamza AKKAOUI",

    'category': 'Website',
    'version': '0.1',

    'depends': ['base',"web","website"],

    'data': [
        'security/access_rights.csv',
        'views/course_management_view.xml',
        'views/user_profiles_view.xml',
        'views/lesson_details_view.xml',
        'views/course_attachments_view.xml',
        'views/homepage_layout.xml',
        'views/course_overview.xml',
        'views/course_ratings_view.xml',
        'views/browse_courses_view.xml'
    ],
    
    'demo': [
        'demonstration.xml',
    ],
    'assets': {
            'web.assets_frontend': [
                            'https://code.jquery.com/jquery-3.5.1.slim.min.js',
                            'https://cdn.jsdelivr.net/npm/@popperjs/core@2.0.8/dist/umd/popper.min.js',
                            'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js'
                            '/e_courses/static/lib/pdfslidesviewer/PDFSlidesViewer.js'
            ]
        }
}
