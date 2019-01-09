# from . course_authors import CourseAuthors
# from . course_subjects import CourseSubjects
# from . course_subject_link import CourseSubjectsLinks
def CourseAuthors():
    from .course_authors import CourseAuthors as ret
    return ret
def CourseSubjects():
    from .course_subjects import CourseSubjects as ret
    return ret
def CourseSubjectsLinks():
    from .course_subject_link import CourseSubjectsLinks as ret
    return ret
def CoursewareOrgs():
    from . courseware_orgs import CoursewareOrgs as ret
    return ret
def CoursewareUserOrgs():
    from . courseware_user_orgs import CoursewareUserOrgs as ret
    return ret